#!/usr/bin/env python3
"""
doc_archive.py - 文档归档工具 v1.0
功能: 检查并归档同类型文档的历史版本
用法: python3 doc_archive.py [--check] [--archive] [--epic "Epic名称"]
更新日期: 2026-04-28
"""

import os
import sys
import re
import shutil
from pathlib import Path
from typing import List, Dict, Tuple
from datetime import datetime

DOC_BASE = "/System/Volumes/Data/Users/wenbo/Documents/文档仓库/数字社区项目"


class DocArchive:
    """文档归档工具"""
    
    def __init__(self, doc_base: str = DOC_BASE):
        self.doc_base = doc_base
        self.archive_count = 0
        self.report = []
    
    def parse_version(self, filename: str) -> Tuple[str, float]:
        """解析版本号，返回(基础名, 版本号)"""
        # 匹配 v1.0, v1.2.3 等格式
        match = re.search(r'-v(\d+\.?\d*)\.md$', filename)
        if match:
            version_str = match.group(1)
            try:
                version = float(version_str)
                base_name = re.sub(r'-v[\d.]+\.md$', '.md', filename)
                return base_name, version
            except:
                pass
        return filename, 0.0
    
    def get_latest_version(self, files: List[str]) -> str:
        """获取最新版本的文档"""
        version_map = {}
        for f in files:
            base, version = self.parse_version(f)
            if version > 0:
                if base not in version_map or version > version_map[base][1]:
                    version_map[base] = (f, version)
        
        return version_map
    
    def check_epic_versions(self, epic_path: str) -> Dict:
        """检查单个Epic的多版本文档"""
        results = {
            "epic": os.path.basename(epic_path),
            "path": epic_path,
            "issues": []
        }
        
        # 定义需要检查版本的文档类型目录
        versioned_dirs = ["产品PRD", "需求拆解结果", "产品操作手册", "技术方案"]
        
        for dirname in versioned_dirs:
            dir_path = os.path.join(epic_path, dirname)
            if not os.path.isdir(dir_path):
                continue
            
            # 获取该目录下所有.md文件
            files = list(Path(dir_path).glob("*.md"))
            if len(files) <= 1:
                continue
            
            # 按基础名分组
            by_basename = {}
            for f in files:
                base, version = self.parse_version(f.name)
                if base not in by_basename:
                    by_basename[base] = []
                by_basename[base].append((f.name, version))
            
            # 检查每组是否有多个版本
            for base, versions in by_basename.items():
                if len(versions) > 1:
                    sorted_versions = sorted(versions, key=lambda x: x[1], reverse=True)
                    latest = sorted_versions[0][0]
                    history = [v[0] for v in sorted_versions[1:]]
                    
                    results["issues"].append({
                        "dir": dirname,
                        "latest": latest,
                        "history": history,
                        "count": len(history)
                    })
        
        return results
    
    def check_all_versions(self) -> List[Dict]:
        """检查所有Epic的多版本文档"""
        all_results = []
        
        for domain in os.listdir(self.doc_base):
            domain_path = os.path.join(self.doc_base, domain)
            if not os.path.isdir(domain_path):
                continue
            
            for epic in os.listdir(domain_path):
                epic_path = os.path.join(domain_path, epic)
                if not os.path.isdir(epic_path):
                    continue
                
                result = self.check_epic_versions(epic_path)
                if result["issues"]:
                    result["domain"] = domain
                    all_results.append(result)
        
        return all_results
    
    def archive_versions(self, issue: Dict, dry_run: bool = True) -> Tuple[int, List[str]]:
        """归档指定问题的历史版本"""
        archived = 0
        archived_files = []
        
        epic_path = issue["path"]
        archive_dir = os.path.join(epic_path, "archive")
        
        for problem in issue["issues"]:
            dir_name = problem["dir"]
            history_files = problem["history"]
            
            # 确保archive目录存在
            if not os.path.exists(archive_dir):
                os.makedirs(archive_dir)
            
            for filename in history_files:
                src = os.path.join(epic_path, dir_name, filename)
                archive_filename = filename.replace(".md", "归档.md")
                dst = os.path.join(archive_dir, archive_filename)
                
                if dry_run:
                    print(f"  [DRY-RUN] 归档: {src} -> {dst}")
                    archived += 1
                    archived_files.append(filename)
                else:
                    shutil.move(src, dst)
                    print(f"  ✅ 归档: {filename} -> archive/")
                    archived += 1
                    archived_files.append(filename)
        
        return archived, archived_files
    
    def run_check(self):
        """执行检查"""
        print("=" * 60)
        print("  文档版本检查")
        print("=" * 60)
        
        results = self.check_all_versions()
        
        if not results:
            print("\n✅ 未发现多版本文档问题")
            return
        
        total_issues = sum(len(r["issues"]) for r in results)
        print(f"\n⚠️ 发现 {len(results)} 个Epic存在多版本文档问题 ({total_issues} 处)")
        
        for result in results:
            print(f"\n📁 {result['domain']}/{result['epic']}")
            for issue in result["issues"]:
                print(f"  ⚠️ {issue['dir']}: {issue['count']}个历史版本")
                print(f"     最新: {issue['latest']}")
                print(f"     待归档: {', '.join(issue['history'])}")
    
    def run_archive(self, dry_run: bool = True):
        """执行归档"""
        action = "检查" if dry_run else "归档"
        print("=" * 60)
        print(f"  文档归档 ({action})")
        print("=" * 60)
        
        results = self.check_all_versions()
        
        if not results:
            print("\n✅ 无需归档的文档")
            return
        
        total_archived = 0
        
        for result in results:
            if result["issues"]:
                print(f"\n📁 {result['domain']}/{result['epic']}")
                archived, files = self.archive_versions(result, dry_run=dry_run)
                total_archived += archived
        
        if dry_run:
            print(f"\n⚠️ 共 {total_archived} 个文件待归档 (使用 --archive 执行)")
        else:
            print(f"\n✅ 共归档 {total_archived} 个文件")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="文档归档工具")
    parser.add_argument("--check", action="store_true", help="仅检查多版本文档")
    parser.add_argument("--archive", action="store_true", help="执行归档")
    parser.add_argument("--epic", type=str, help="指定Epic名称")
    
    args = parser.parse_args()
    
    archiver = DocArchive()
    
    if args.check or not args.archive:
        archiver.run_check()
    
    if args.archive:
        archiver.run_archive(dry_run=False)


if __name__ == "__main__":
    main()
