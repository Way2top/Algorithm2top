import sys
import os

# --- 这部分代码会直接打印到你的终端或 DAP 输出窗口 ---
print("=" * 50)
print("DEBUGGER RUNTIME ENVIRONMENT CHECK")
print(f"Python Executable Path: {sys.executable}")
print(f"Python Version: {sys.version}")

# 检查 Neovim 是否继承了 Conda 环境变量
conda_env = os.getenv("CONDA_DEFAULT_ENV")
conda_prefix = os.getenv("CONDA_PREFIX")
print(f"Conda Env (CONDA_DEFAULT_ENV): {conda_env}")
print(f"Conda Prefix (CONDA_PREFIX): {conda_prefix}")
print("=" * 50)
# --- 结束打印 ---

# 在下面这一行设置断点
name = "debugger"
print(f"Hello, {name}")  # <--- 在这里设置断点

print("Debug session finished.")
