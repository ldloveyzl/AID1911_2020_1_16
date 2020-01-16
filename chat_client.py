"""
char room 客户端
"""
from socket import *
import os
import sys

# 服务器地址
ADDR = ('127.0.0.1', 8888)

# 发送消息
def send_msg(s,name):
    while True:
        try:
            text = input("消息:")
        except KeyboardInterrupt:
            text = 'quit'
        if not text:
            continue
        if text == 'quit':
            msg = "QUIT " + name
            s.sendto(msg.encode(),ADDR) # 退出
            sys.exit("退出聊天室")
        msg = "CHAT %s %s"%(name,text)
        s.sendto(msg.encode(),ADDR)

# 接受消息
def recv_msg(s):
    while True:
        data,addr = s.recvfrom(2048)
        # 从服务器接受到QUIT表示退出
        if data == b'QUIT':
            sys.exit()
        print(data.decode()+"\n消息：",end="")

# 登录处理
def do_login(s):
    while True:
        name = input("你的昵称:")
        msg = "LOGIN " + name
        s.sendto(msg.encode(), ADDR)  # 发请求
        # 接受反馈
        data,addr = s.recvfrom(128)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            return name
        else:
            # 得到失败原因
            print(data.decode())

# 网络搭建
def main():
    s = socket(AF_INET, SOCK_DGRAM)
    name = do_login(s)
    if name:
        # 如果登录成功，创建新的进程
        pid = os.fork()
        if pid < 0:
            sys.exit("服务器异常....")
        elif pid == 0:
            send_msg(s,name) # 发送消息
        else:
            recv_msg(s) # 收消息


if __name__ == '__main__':
    main()
