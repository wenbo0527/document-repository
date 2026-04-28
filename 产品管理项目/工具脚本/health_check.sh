#!/bin/bash
# health_check.sh - 产品管理系统健康检查脚本
# 版本: v1.0
# 更新日期: 2026-04-28
# 维护者: Tony Stark

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 日志函数
log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# 检查Neo4j服务
check_neo4j() {
    log_info "检查Neo4j服务状态..."
    
    if curl -s http://localhost:7474 > /dev/null 2>&1; then
        log_info "✅ Neo4j服务正常运行"
        return 0
    else
        log_error "❌ Neo4j服务未运行"
        log_info "尝试启动Neo4j..."
        /opt/homebrew/Cellar/neo4j/*/bin/neo4j start 2>/dev/null || true
        sleep 5
        if curl -s http://localhost:7474 > /dev/null 2>&1; then
            log_info "✅ Neo4j服务已启动"
            return 0
        else
            log_error "❌ Neo4j服务启动失败"
            return 1
        fi
    fi
}

# 检查节点数量
check_nodes() {
    log_info "检查节点数量..."
    
    python3 << 'EOF'
import sys
sys.path.insert(0, '/Users/wenbo/Documents/project/product_managment/backend-python')
from neo4j import GraphDatabase

uri = 'bolt://localhost:7687'
driver = GraphDatabase.driver(uri, auth=('neo4j', 'password123'))

# 基线值
expected = {
    'ProductDomain': {'min': 6, 'max': 6, 'desc': '产品域'},
    'Epic': {'min': 22, 'max': 22, 'desc': 'Epic'},
    'Feature': {'min': 120, 'max': 160, 'desc': 'Feature'},
    'Story': {'min': 200, 'max': 220, 'desc': 'Story'}
}

try:
    with driver.session() as session:
        result = session.run('''
        MATCH (n) 
        RETURN labels(n)[0] as label, count(*) as count
        ORDER BY label
        ''')
        
        all_ok = True
        for r in result:
            label = r['label']
            count = r['count']
            
            if label in expected:
                exp = expected[label]
                if exp['min'] <= count <= exp['max']:
                    status = "✅"
                else:
                    status = "⚠️"
                    all_ok = False
                print(f"  {status} {label}({exp['desc']}): {count} (期望 {exp['min']}-{exp['max']})")
        
        if all_ok:
            print("\n✅ 所有节点数量正常")
        else:
            print("\n⚠️ 存在节点数量异常")
            
except Exception as e:
    print(f"❌ 查询失败: {e}")
finally:
    driver.close()
EOF
}

# 检查Feature粒度
check_feature_granularity() {
    log_info "检查Feature粒度(3-15为正常)..."
    
    python3 << 'EOF'
import sys
sys.path.insert(0, '/Users/wenbo/Documents/project/product_managment/backend-python')
from neo4j import GraphDatabase

uri = 'bolt://localhost:7687'
driver = GraphDatabase.driver(uri, auth=('neo4j', 'password123'))

try:
    with driver.session() as session:
        result = session.run('''
        MATCH (e:Epic)-[:CONTAINS]->(f:Feature)
        WITH e.name as epic, count(f) as cnt
        RETURN epic, cnt
        ORDER BY cnt DESC
        ''')
        
        all_ok = True
        for r in result:
            epic = r['epic']
            cnt = r['cnt']
            
            if cnt < 3:
                status = "⚠️ 偏少"
                all_ok = False
            elif cnt > 15:
                status = "⚠️ 偏多"
                all_ok = False
            else:
                status = "✅ 正常"
            
            print(f"  {status} {epic}: {cnt}")
        
        if all_ok:
            print("\n✅ 所有Epic Feature粒度正常")
        else:
            print("\n⚠️ 存在粒度异常的Epic")
            
except Exception as e:
    print(f"❌ 查询失败: {e}")
finally:
    driver.close()
EOF
}

# 检查重复节点
check_duplicates() {
    log_info "检查重复节点..."
    
    python3 << 'EOF'
import sys
sys.path.insert(0, '/Users/wenbo/Documents/project/product_managment/backend-python')
from neo4j import GraphDatabase

uri = 'bolt://localhost:7687'
driver = GraphDatabase.driver(uri, auth=('neo4j', 'password123'))

try:
    with driver.session() as session:
        # 检查重复Epic
        result = session.run('''
        MATCH (e:Epic)
        WITH e.name as ename, count(*) as cnt
        WHERE cnt > 1
        RETURN ename, cnt
        ORDER BY cnt DESC
        ''')
        
        epic_dups = []
        for r in result:
            print(f"  ⚠️ Epic重名: {r['ename']} ({r['cnt']}个)")
            epic_dups.append(r['ename'])
        
        if not epic_dups:
            print("  ✅ 无重复Epic")
        
        # 检查重复Feature
        result = session.run('''
        MATCH (e:Epic)-[:CONTAINS]->(f:Feature)
        WITH e.name as epic, f.name as fname, count(*) as cnt
        WHERE cnt > 1
        RETURN epic, fname, cnt
        ORDER BY epic, cnt DESC
        ''')
        
        feature_dups = []
        for r in result:
            print(f"  ⚠️ Feature重名: {r['epic']}/{r['fname']} ({r['cnt']}个)")
            feature_dups.append(f"{r['epic']}/{r['fname']}")
        
        if not feature_dups:
            print("  ✅ 无重复Feature")
            
except Exception as e:
    print(f"❌ 查询失败: {e}")
finally:
    driver.close()
EOF
}

# 检查层级关系
check_hierarchy() {
    log_info "检查层级关系完整性..."
    
    python3 << 'EOF'
import sys
sys.path.insert(0, '/Users/wenbo/Documents/project/product_managment/backend-python')
from neo4j import GraphDatabase

uri = 'bolt://localhost:7687'
driver = GraphDatabase.driver(uri, auth=('neo4j', 'password123'))

try:
    with driver.session() as session:
        checks = [
            ("ProductDomain→Epic", "MATCH (pd:ProductDomain)-[:CONTAINS]->(e:Epic) RETURN count(e) as cnt"),
            ("Epic→Feature", "MATCH (e:Epic)-[:CONTAINS]->(f:Feature) RETURN count(f) as cnt"),
            ("Feature→Story", "MATCH (f:Feature)-[:CONTAINS]->(s:Story) RETURN count(s) as cnt"),
        ]
        
        for name, query in checks:
            result = session.run(query)
            cnt = result.single()['cnt']
            if cnt > 0:
                print(f"  ✅ {name}: {cnt}")
            else:
                print(f"  ⚠️ {name}: {cnt} (可能异常)")
                
except Exception as e:
    print(f"❌ 查询失败: {e}")
finally:
    driver.close()
EOF
}

# 检查ProductDomain分布
check_domain_distribution() {
    log_info "检查ProductDomain Epic分布..."
    
    python3 << 'EOF'
import sys
sys.path.insert(0, '/Users/wenbo/Documents/project/product_managment/backend-python')
from neo4j import GraphDatabase

uri = 'bolt://localhost:7687'
driver = GraphDatabase.driver(uri, auth=('neo4j', 'password123'))

expected_domains = {
    '数字社区': 4,
    '数字营销': 5,
    '数字风险': 2,
    '数据发现': 5,
    '数据探索': 3,
    '数据管理': 3
}

try:
    with driver.session() as session:
        result = session.run('''
        MATCH (pd:ProductDomain)-[:CONTAINS]->(e:Epic)
        RETURN pd.name as domain, count(e) as epic_count
        ORDER BY pd.name
        ''')
        
        all_ok = True
        for r in result:
            domain = r['domain']
            cnt = r['epic_count']
            exp = expected_domains.get(domain, 0)
            
            if cnt == exp:
                status = "✅"
            else:
                status = "⚠️"
                all_ok = False
            
            print(f"  {status} {domain}: {cnt} Epic (期望 {exp})")
        
        if all_ok:
            print("\n✅ ProductDomain分布正常")
        else:
            print("\n⚠️ ProductDomain分布异常")
            
except Exception as e:
    print(f"❌ 查询失败: {e}")
finally:
    driver.close()
EOF
}

# 主函数
main() {
    echo "========================================"
    echo "   产品管理系统健康检查"
    echo "   $(date '+%Y-%m-%d %H:%M:%S')"
    echo "========================================"
    echo ""
    
    # 1. 检查Neo4j服务
    check_neo4j || exit 1
    echo ""
    
    # 2. 检查节点数量
    check_nodes
    echo ""
    
    # 3. 检查ProductDomain分布
    check_domain_distribution
    echo ""
    
    # 4. 检查Feature粒度
    check_feature_granularity
    echo ""
    
    # 5. 检查重复节点
    check_duplicates
    echo ""
    
    # 6. 检查层级关系
    check_hierarchy
    echo ""
    
    echo "========================================"
    echo "   检查完成"
    echo "========================================"
}

# 执行主函数
main
