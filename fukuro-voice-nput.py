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
pattern = r'WHYPO WORD=\"(.*)\" CLASSID=\"((?!<).*)\"'
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
                       # 初期化コマンド
                       if (u('フクロウ') in word) or (u('フクロ') in word):
                            if(shouldListen == False):
                                print ("ユーザ：{}".format(word))
                                print ("フクロウ：はい、何でしょうか？")
                                print("-------------------")
                            else:
                                print ("ユーザ：{}".format(word))
                                print ("フクロウ：はい、聞いていますよ。何でしょうか？")
                                print("-------------------")
                            # 初期化
                            tempRegisterDetail = {
                                "command": "",
                                "id": None,
                                "name": ""
                            }
                            shouldListen = True
                       elif shouldListen == True :
                            print ("ユーザ：{}".format(word))
                            if (u('登録') in word):   # 命令
                                tempRegisterDetail.update({ "command": "登録" })
                                print ("tempRegisterDetail: {}".format(tempRegisterDetail))
                                print ("フクロウ：登録しますね。idは何？")
                                print("-------------------")
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
                                    print ("フクロウ：お名前は？")
                                    print("-------------------")
                            # name 取得
                            elif (tempRegisterDetail["command"] == "登録") and (tempRegisterDetail["id"] != None) and (tempRegisterDetail["name"] == ""):
                                # TODO: 名前を識別できる機能を追加
                                tempRegisterDetail.update({ "name": word})
                                print ("tempRegisterDetail: {}".format(tempRegisterDetail))
                                print ("idは{0},名前は{1}で登録して、よろしいですか？はい　か　いいえで答えてください".format(tempRegisterDetail["id"], tempRegisterDetail["name"]))
                                print("-------------------")
                            elif (tempRegisterDetail["command"] == "登録") and (tempRegisterDetail["id"] != None) and (tempRegisterDetail["name"] != ""):
                                if(word == "はい"):
                                    # TODO: カメラ認識でユーザを登録
                                    shouldListen = False
                                    tempRegisterDetail = {
                                        "command": "",
                                        "id": None,
                                        "name": ""
                                    }
                                    print ("tempRegisterDetail: {}".format(tempRegisterDetail))
                                    print ("フクロウ：登録しましたので、終了しますね")
                                    print("-------------------")
                                elif(word == "いいえ"):
                                    shouldListen = False
                                    tempRegisterDetail = {
                                        "command": "",
                                        "id": None,
                                        "name": ""
                                    }
                                    print ("tempRegisterDetail: {}".format(tempRegisterDetail))
                                    print ("フクロウ：終了しますね。１からやり直してね。")
                                    print("-------------------")
                                else:
                                    print ("フクロウ：はい　か　いいえで答えてくださいね")
                            else:
                                print("フクロウ：以下の望ましいコマンドのいずれかを言ってください")
                                print("フクロウ：1. 登録")
                                print("フクロウ：以上です。")
                                print("-------------------")
                                
            buff.close()
            buff = StringIO(u(''))
            if lines[len(lines)-1] != '.':
            	buff.write(lines[len(lines)-1])

except socket.error:
    print('socket error')
except KeyboardInterrupt:
    pass

sock.close()
