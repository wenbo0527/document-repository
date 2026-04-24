#!/usr/bin/env python3
"""
Neo4j 产品域修复脚本

用法:
    python3 repair_domain.py <domain_code>
    
示例:
    python3 repair_domain.py PD-MKT
    python3 repair_domain.py PD-COM
"""

import sys
import json
from neo4j import GraphDatabase

# Neo4j 配置
URI = 'bolt://localhost:7687'
AUTH = ('neo4j', 'password123')

# 产品域配置
DOMAIN_CONFIG = {
    'PD-MKT': {
        'name': '数字营销',
        'epics': [
            {
                'uri': 'Epic:EPIC-MKT-REACH',
                'name': '触达系统',
                'features': [
                    {'uri': 'Feature:FEAT-MKT-REACH-IDX', 'name': '触达首页', 'code_path': 'touch/index.vue'},
                    {'uri': 'Feature:FEAT-MKT-REACH-SYS', 'name': '系统管理', 'code_path': 'touch/system/'},
                    {'uri': 'Feature:FEAT-MKT-REACH-POL', 'name': '策略管理', 'code_path': 'touch/policy/'},
                    {'uri': 'Feature:FEAT-MKT-REACH-CH', 'name': '渠道管理', 'code_path': 'touch/channel/'},
                    {'uri': 'Feature:FEAT-MKT-REACH-QRY', 'name': '触达查询', 'code_path': 'touch/query/'},
                ]
            },
            {
                'uri': 'Epic:EPIC-MKT-BENEFIT',
                'name': '权益中心',
                'features': [
                    {'uri': 'Feature:FEAT-MKT-BENEFIT-IDX', 'name': '权益首页', 'code_path': 'benefits/index.vue'},
                    {'uri': 'Feature:FEAT-MKT-BENEFIT-CONFIG', 'name': '权益配置', 'code_path': 'benefits/config/'},
                    {'uri': 'Feature:FEAT-MKT-BENEFIT-STATS', 'name': '权益统计', 'code_path': 'benefits/stats/'},
                    {'uri': 'Feature:FEAT-MKT-BENEFIT-GLOBAL', 'name': '全局管理', 'code_path': 'benefits/global/'},
                ]
            },
            {
                'uri': 'Epic:EPIC-MKT-CROWD',
                'name': '客群中心',
                'features': [
                    {'uri': 'Feature:FEAT-MKT-CROWD-SYS', 'name': '系统管理', 'code_path': 'crowd/system/'},
                    {'uri': 'Feature:FEAT-MKT-CROWD-LIST', 'name': '人群列表', 'code_path': 'crowd/list/'},
                    {'uri': 'Feature:FEAT-MKT-CROWD-EVENT', 'name': '事件管理', 'code_path': 'crowd/event/'},
                    {'uri': 'Feature:FEAT-MKT-CROWD-IDMAP', 'name': 'ID-mapping', 'code_path': 'crowd/idmap/'},
                ]
            },
            {
                'uri': 'Epic:EPIC-MKT-CANVAS',
                'name': '营销画布',
                'features': [
                    {'uri': 'Feature:FEAT-MKT-CANVAS-LIST', 'name': '画布列表', 'code_path': 'canvas/list.vue'},
                    {'uri': 'Feature:FEAT-MKT-CANVAS-DETAIL', 'name': '画布详情', 'code_path': 'canvas/detail/'},
                ]
            },
            {
                'uri': 'Epic:EPIC-MKT-SALES',
                'name': '人工电销工作台',
                'features': [
                    {'uri': 'Feature:FEAT-MKT-SALES-ORG', 'name': '组织管理', 'code_path': 'sales/org/'},
                    {'uri': 'Feature:FEAT-MKT-SALES-TASK', 'name': '任务管理', 'code_path': 'sales/task/'},
                    {'uri': 'Feature:FEAT-MKT-SALES-WORKBENCH', 'name': '客户工作台', 'code_path': 'sales/workbench/'},
                    {'uri': 'Feature:FEAT-MKT-SALES-QC', 'name': '质量管理', 'code_path': 'sales/qc/'},
                    {'uri': 'Feature:FEAT-MKT-SALES-COST', 'name': '费用管理', 'code_path': 'sales/cost/'},
                    {'uri': 'Feature:FEAT-MKT-SALES-SYS', 'name': '系统管理', 'code_path': 'sales/system/'},
                    {'uri': 'Feature:FEAT-MKT-SALES-DASHBOARD', 'name': '数据看板', 'code_path': 'sales/dashboard/'},
                ]
            },
        ]
    },
    'PD-COM': {
        'name': '数字社区',
        'epics': [
            {
                'uri': 'Epic:EPIC-COM-PERM',
                'name': '权限管理',
                'features': [
                    {'uri': 'Feature:FEAT-COM-PERM-APP', 'name': '权限申请', 'code_path': 'perm/apply.vue'},
                    {'uri': 'Feature:FEAT-COM-PERM-APPROVAL', 'name': '权限审批', 'code_path': 'perm/approval.vue'},
                    {'uri': 'Feature:FEAT-COM-PERM-PROGRESS', 'name': '权限进度', 'code_path': 'perm/progress.vue'},
                    {'uri': 'Feature:FEAT-COM-PERM-DATA', 'name': '数据权限', 'code_path': 'perm/data.vue'},
                ]
            },
            {
                'uri': 'Epic:EPIC-COM-CONTENT',
                'name': '内容管理',
                'features': [
                    {'uri': 'Feature:FEAT-COM-CONTENT-LIST', 'name': '内容列表', 'code_path': 'content/list.vue'},
                    {'uri': 'Feature:FEAT-COM-CONTENT-CREATE', 'name': '内容创建', 'code_path': 'content/create.vue'},
                    {'uri': 'Feature:FEAT-COM-CONTENT-CATEGORY', 'name': '分类管理', 'code_path': 'content/category.vue'},
                ]
            },
            {
                'uri': 'Epic:EPIC-COM-NOTICE',
                'name': '通知管理',
                'features': [
                    {'uri': 'Feature:FEAT-COM-NOTICE-LIST', 'name': '通知列表', 'code_path': 'notice/list.vue'},
                    {'uri': 'Feature:FEAT-COM-NOTICE-CREATE', 'name': '通知创建', 'code_path': 'notice/create.vue'},
                    {'uri': 'Feature:FEAT-COM-NOTICE-APPROVAL', 'name': '通知审批', 'code_path': 'notice/approval.vue'},
                ]
            },
            {
                'uri': 'Epic:EPIC-COM-PORTAL',
                'name': '门户管理',
                'features': [
                    {'uri': 'Feature:FEAT-COM-PORTAL-HOME', 'name': '门户首页', 'code_path': 'portal/home.vue'},
                    {'uri': 'Feature:FEAT-COM-PORTAL-UPLOAD', 'name': '上传管理', 'code_path': 'portal/upload.vue'},
                    {'uri': 'Feature:FEAT-COM-PORTAL-DOCS', 'name': '文档管理', 'code_path': 'portal/docs.vue'},
                    {'uri': 'Feature:FEAT-COM-PORTAL-TODO', 'name': '待办管理', 'code_path': 'portal/todo.vue'},
                ]
            },
        ]
    },
}

def repair_domain(domain_code):
    """修复指定产品域的 Epic/Feature 层级"""
    
    if domain_code not in DOMAIN_CONFIG:
        print(f"❌ 未知的产品域: {domain_code}")
        print(f"   可用的产品域: {', '.join(DOMAIN_CONFIG.keys())}")
        return False
    
    config = DOMAIN_CONFIG[domain_code]
    domain_name = config['name']
    epics = config['epics']
    
    print(f"🔧 开始修复 {domain_code} ({domain_name})")
    print("=" * 50)
    
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        with driver.session() as session:
            # Step 1: 确保 ProductDomain 存在
            print(f"\n【1】确保 ProductDomain 存在...")
            session.run('''
                MERGE (d:ProductDomain {uri: $domain_uri})
                SET d.name = $domain_name, d.updated_at = datetime()
            ''', domain_uri=f'ProductDomain:{domain_code}', domain_name=domain_name)
            print(f"   ✅ ProductDomain:{domain_code} 已确认")
            
            # Step 2: 处理每个 Epic
            total_features = 0
            for epic in epics:
                epic_uri = epic['uri']
                epic_name = epic['name']
                features = epic['features']
                
                print(f"\n【2】处理 Epic: {epic_name}")
                
                # 2.1 确保 Epic 存在
                session.run('''
                    MERGE (e:Epic {uri: $epic_uri})
                    SET e.name = $epic_name,
                        e.domain = $domain_code,
                        e.status = 'planning',
                        e.updated_at = datetime()
                ''', epic_uri=epic_uri, epic_name=epic_name, domain_code=domain_code)
                print(f"   ✅ Epic 已创建: {epic_uri}")
                
                # 2.2 建立 ProductDomain -> Epic 关系
                session.run('''
                    MATCH (d:ProductDomain {uri: $domain_uri})
                    MATCH (e:Epic {uri: $epic_uri})
                    MERGE (d)-[:CONTAINS]->(e)
                ''', domain_uri=f'ProductDomain:{domain_code}', epic_uri=epic_uri)
                
                # 2.3 处理每个 Feature
                for feat in features:
                    feat_uri = feat['uri']
                    feat_name = feat['name']
                    code_path = feat.get('code_path', '')
                    
                    session.run('''
                        MERGE (f:Feature {uri: $feat_uri})
                        SET f.name = $feat_name,
                            f.code_path = $code_path,
                            f.status = 'planning',
                            f.updated_at = datetime()
                    ''', feat_uri=feat_uri, feat_name=feat_name, code_path=code_path)
                    
                    # 2.4 建立 Epic -> Feature 关系
                    session.run('''
                        MATCH (e:Epic {uri: $epic_uri})
                        MATCH (f:Feature {uri: $feat_uri})
                        MERGE (e)-[:CONTAINS]->(f)
                    ''', epic_uri=epic_uri, feat_uri=feat_uri)
                    
                    total_features += 1
                    print(f"   ✅ Feature 已创建: {feat_name}")
            
            print(f"\n{'=' * 50}")
            print(f"✅ {domain_code} 修复完成!")
            print(f"   Epic 数量: {len(epics)}")
            print(f"   Feature 数量: {total_features}")
            
            # Step 3: 验证结果
            print(f"\n【3】验证结果...")
            result = session.run('''
                MATCH (d:ProductDomain {uri: $domain_uri})-[:CONTAINS]->(e:Epic)-[:CONTAINS]->(f:Feature)
                RETURN count(DISTINCT e) as epic_count, count(DISTINCT f) as feature_count
            ''', domain_uri=f'ProductDomain:{domain_code}').single()
            
            print(f"   Epic: {result['epic_count']}")
            print(f"   Feature: {result['feature_count']}")
            
            if result['epic_count'] == len(epics) and result['feature_count'] == total_features:
                print(f"\n🎉 验证通过!")
            else:
                print(f"\n⚠️ 验证异常，请检查!")
            
            return True
            
    except Exception as e:
        print(f"❌ 修复失败: {e}")
        return False
    finally:
        driver.close()

def status_check(domain_code=None):
    """检查产品域状态"""
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        with driver.session() as session:
            if domain_code:
                # 检查指定产品域
                result = session.run('''
                    MATCH (d:ProductDomain {uri: $domain_uri})-[:CONTAINS]->(e:Epic)-[:CONTAINS]->(f:Feature)
                    RETURN d.uri as domain, count(DISTINCT e) as epic_count, count(DISTINCT f) as feature_count
                ''', domain_uri=f'ProductDomain:{domain_code}')
                row = result.single()
                if row:
                    print(f"📊 {domain_code}: {row['epic_count']} Epic, {row['feature_count']} Feature")
                else:
                    print(f"❌ {domain_code}: 无数据或结构不完整")
            else:
                # 检查所有产品域
                print("📊 所有产品域状态:")
                result = session.run('''
                    MATCH (d:ProductDomain)
                    OPTIONAL MATCH (d)-[:CONTAINS]->(e:Epic)-[:CONTAINS]->(f:Feature)
                    RETURN d.uri as domain, count(DISTINCT e) as epic_count, count(DISTINCT f) as feature_count
                    ORDER BY d.uri
                ''')
                for row in result:
                    domain = row['domain'].replace('ProductDomain:', '')
                    print(f"  {domain}: {row['epic_count']} Epic, {row['feature_count']} Feature")
    finally:
        driver.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        print("\n可用命令:")
        print("  python3 repair_domain.py status          # 查看所有产品域状态")
        print("  python3 repair_domain.py status PD-MKT   # 查看指定产品域状态")
        print("  python3 repair_domain.py PD-MKT           # 修复 PD-MKT")
        sys.exit(1)
    
    cmd = sys.argv[1].upper()
    
    if cmd == 'STATUS':
        if len(sys.argv) >= 3:
            status_check(sys.argv[2].upper())
        else:
            status_check()
    elif cmd in DOMAIN_CONFIG:
        repair_domain(cmd)
    else:
        print(f"❌ 未知命令或产品域: {sys.argv[1]}")
        print(f"   可用的产品域: {', '.join(DOMAIN_CONFIG.keys())}")
        sys.exit(1)
