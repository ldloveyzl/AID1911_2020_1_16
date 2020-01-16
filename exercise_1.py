"""
下面的函数要执行10次,希望在4秒之内执行完
"""
import os
import time

def fun():
   print('开始执行啦：',os.getpid())
   time.sleep(3)
   print("结束执行啦")

st = time.time()

for i in range(10):
    pid = os.fork()
    if pid == 0:
        fun()
        print("Time:",time.time()-st)
        os._exit(0) # 子进程在执行完一个函数之后就让他结束
