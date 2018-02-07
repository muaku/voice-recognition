# -*- coding: utf-8 -*-
import socket
from io import StringIO
import re
import subprocess

try:
    unicode # python2
    def u(str): return str.decode('utf-8')
    pass
except: # python3
    def u(str): return str
    pass

host = '127.0.0.1'
port = 10500
bufsize = 1024
shouldListen = False
tempRegisterDetail = ["", "",""]     # 3 param: 0 命令, 1:

buff = StringIO(u(''))
pattern = r'WHYPO WORD=\"(.*)\" CLASSID'
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    while True:
        data = sock.recv(bufsize)
        buff.write(data.decode('utf-8'))
        data = buff.getvalue().replace('> ', '>\n ')
        if '\n' in data:
            lines = data.splitlines()
            for i in range(len(lines)-1):
                if lines[i] != '.':
                   m = re.search(pattern, lines[i])
                   if m:
                       word = m.group(1)
#                       print (word)
                       # 処理の判断
                       if (u('フクロウ') in word) or (u('フクロ') in word) or (shouldListen == True):
                            shouldListen = True     # 次の会話を聞く
                            if (u('登録') in word):
                                tempRegisterDetail[0] = "登録"
                                # フクロウ：idのnumberを言ってください
                            elif (tempRegisterDetail[0] == "登録") and (tempRegisterDetail[1] == ""):
                                tempRegisterDetail[1] = word
                            elif (tempRegisterDetail[0] == "登録") and (tempRegisterDetail[1] != ""):
                                tempRegisterDetail[2] = word
                                print ("tempRegisterDetail: {}".format(tempRegisterDetail))
                                # TODO: カメラ認識でユーザを登録
                                shouldListen = False
                                tempRegisterDetail = ["", "", ""]
            buff.close()
            buff = StringIO(u(''))
            if lines[len(lines)-1] != '.':
            	buff.write(lines[len(lines)-1])

except socket.error:
    print('socket error')
except KeyboardInterrupt:
    pass

sock.close()
