"""
模拟僵尸进程产生
"""
import os
import sys

import signal
# 忽略子进程退出行为，让操作系统处理
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("child process:",os.getpid())
    os._exit(2)
else:
    """
    wait 方法处理僵尸
    """
    # p,status = os.wait()
    # print("PID:",p)
    # print("Status:",os.WEXITSTATUS(status))
    while True:
        pass

