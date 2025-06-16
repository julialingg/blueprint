#!/bin/bash

echo "Running script to create PR branches..."

# 确保使用的是 WSL 中的 Python
python3 create_pr_branches.py

# 保持窗口暂停（可选）
read -p "Press enter to continue"
