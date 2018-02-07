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
#tempRegisterDetail = ["", "",""]     # 3 param: 0 命令, 1:
tempRegisterDetail = {
    "command": "",
    "id": None,
    "name": ""
}

buff = StringIO(u(''))
pattern = r'WHYPO WORD=\"(.*)\" CLASSID=\"((?!</s>).*)\"'
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
                       # 処理の判断
                       if (u('フクロウ') in word) or (u('フクロ') in word) or (shouldListen == True):
                            shouldListen = True     # 次の会話を聞く
                            print (word)
                            print ("はい、何でしょうか？")
                            if (u('登録') in word):   # 命令
                                tempRegisterDetail.update({ "command": "登録" })
                                print ("tempRegisterDetail: {}".format(tempRegisterDetail))
                                print ("登録しますね。idは何？")
                                # フクロウ：idのnumberを言ってください
                            # id 取得
                            elif (tempRegisterDetail["command"] == "登録") and (tempRegisterDetail["id"] == None):
                                # 数字のみゲット
                                val = "".join(filter(str.isdigit, word))
                                print ("val: {}".format(val))
                                if(val != ""):
                                    id = int(val)
                                    print (id)
                                    tempRegisterDetail.update({ "id": id})
                                    print ("tempRegisterDetail: {}".format(tempRegisterDetail))
                                    print ("お名前は？")
                            # name 取得
                            elif (tempRegisterDetail["command"] == "登録") and (tempRegisterDetail["id"] != None):
                                # TODO: 名前を識別できる機能を追加
                                tempRegisterDetail.update({ "name": word})
                                print ("tempRegisterDetail: {}".format(tempRegisterDetail))
                                # TODO: カメラ認識でユーザを登録
                                shouldListen = False
                                tempRegisterDetail = {
                                    "command": "",
                                    "id": None,
                                    "name": ""
                                }
                                print ("tempRegisterDetail: {}".format(tempRegisterDetail))
                                print ("登録しましたので、終了しますね")
            buff.close()
            buff = StringIO(u(''))
            if lines[len(lines)-1] != '.':
            	buff.write(lines[len(lines)-1])

except socket.error:
    print('socket error')
except KeyboardInterrupt:
    pass

sock.close()
