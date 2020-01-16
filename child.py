"""
二级子进程防止僵尸
"""
import time
import os

# 孙
def fun1():
    print("写代码")
    time.sleep(3)
    print("写完了")

# 父
def fun2():
    print("改代码")
    time.sleep(4)
    print("改完了")

p1 = os.fork()
if p1 < 0:
    print("Error")
elif p1 == 0:
    p2 = os.fork()
    if p2 == 0:
        fun1() # 二级子进程
    else:
        # 一级子进程
        os._exit(0)
else:
    os.wait() # 处理子进程
    fun2() # 父进程执行一件事
