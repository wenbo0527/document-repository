#!/usr/bin/env python3
"""
health_check.py - Neo4j 数据质量验证
实际脚本位于 backend-python 目录，此处为包装调用
"""
import subprocess, sys
script_path = "/Users/wenbo/Documents/project/product_managment/backend-python/health_check.py"
result = subprocess.run(["python3", script_path] + sys.argv[1:], capture_output=False)
sys.exit(result.returncode)
