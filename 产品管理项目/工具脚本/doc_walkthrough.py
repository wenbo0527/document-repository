#!/usr/bin/env python3
"""
doc_walkthrough.py - 文档走查工具 v1.0
产品域 -> Epic -> 本地文档 -> Neo4j Feature 对齐检查
更新日期: 2026-04-28
"""

import os
import sys
from pathlib import Path
from typing import Dict, List

NEO4J_URI = "bolt://localhost:7687"
NEO4J_AUTH = ("neo4j", "password123")
DOC_BASE = "/System/Volumes/Data/Users/wenbo/Documents/文档仓库/数字社区项目"

sys.path.insert(0, '/Users/wenbo/Documents/project/product_managment/backend-python')

from neo4j import GraphDatabase


class DocWalkthrough:
    def __init__(self):
        self.driver = GraphDatabase.driver(NEO4J_URI, auth=NEO4J_AUTH)
        self.standard_dirs = ["业务需求入口", "需求拆解结果", "产品PRD", "产品操作手册", "技术方案"]
    
    def close(self):
        self.driver.close()
    
    def get_neo4j_data(self) -> Dict:
        with self.driver.session() as session:
            result = session.run('''
            MATCH (pd:ProductDomain)-[:CONTAINS]->(e:Epic)
            RETURN pd.name as domain, e.name as epic
            ORDER BY pd.name, e.name
            ''')
            data = {}
            for r in result:
                domain = r['domain']
                epic = r['epic']
                if domain not in data:
                    data[domain] = []
                data[domain].append(epic)
            return data
    
    def get_neo4j_feature_count(self, epic_name: str) -> int:
        with self.driver.session() as session:
            result = session.run('''
            MATCH (e:Epic {name: $name})-[:CONTAINS]->(f:Feature)
            RETURN count(f) as cnt
            ''', name=epic_name)
            record = result.single()
            return record['cnt'] if record else 0
    
    def check_epic_directory(self, epic_path: str) -> Dict:
        result = {"exists": os.path.isdir(epic_path), "dirs": {}, "total_files": 0}
        if not result["exists"]:
            return result
        for d in self.standard_dirs:
            dir_path = os.path.join(epic_path, d)
            if os.path.isdir(dir_path):
                files = list(Path(dir_path).glob("*.md"))
                result["dirs"][d] = {"exists": True, "file_count": len(files)}
                result["total_files"] += len(files)
            else:
                result["dirs"][d] = {"exists": False, "file_count": 0}
        return result
    
    def walkthrough_domain(self, domain: str) -> Dict:
        domain_path = os.path.join(DOC_BASE, domain)
        if not os.path.isdir(domain_path):
            return {"error": f"目录不存在: {domain_path}"}
        
        result = {"domain": domain, "epics": {}}
        local_epics = [d for d in os.listdir(domain_path) if os.path.isdir(os.path.join(domain_path, d))]
        neo4j_data = self.get_neo4j_data()
        neo4j_epics = neo4j_data.get(domain, [])
        
        result["local_epic_count"] = len(local_epics)
        result["neo4j_epic_count"] = len(neo4j_epics)
        result["epic_match"] = set(local_epics) == set(neo4j_epics)
        
        for epic in local_epics:
            epic_path = os.path.join(domain_path, epic)
            neo4j_feature_count = self.get_neo4j_feature_count(epic)
            dir_check = self.check_epic_directory(epic_path)
            result["epics"][epic] = {
                "path": epic_path,
                "neo4j_feature_count": neo4j_feature_count,
                "directory_check": dir_check
            }
        return result
    
    def walkthrough_all(self) -> List[Dict]:
        results = []
        if not os.path.isdir(DOC_BASE):
            print(f"[ERROR] 文档目录不存在: {DOC_BASE}")
            return results
        
        domains = sorted([d for d in os.listdir(DOC_BASE) if os.path.isdir(os.path.join(DOC_BASE, d))])
        for domain in domains:
            print(f"\n[WALK] {domain}")
            result = self.walkthrough_domain(domain)
            results.append(result)
            local = result.get('local_epic_count', 0)
            neo4j = result.get('neo4j_epic_count', 0)
            match = "OK" if result.get('epic_match') else "MISMATCH"
            print(f"  Local Epic: {local}, Neo4j Epic: {neo4j}, Match: {match}")
        return results


def main():
    print("=" * 50)
    print("   Doc Walkthrough Tool v1.0")
    print("=" * 50)
    
    walker = DocWalkthrough()
    try:
        results = walker.walkthrough_all()
        print("\n" + "=" * 50)
        print("   Walkthrough Complete")
        print("=" * 50)
    finally:
        walker.close()


if __name__ == "__main__":
    main()
