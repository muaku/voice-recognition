import os
import sys
import subprocess

argv = sys.argv
id = sys.argv[1]
name = sys.argv[2]
# print (argv)
# id と name の入力が必要
subprocess.Popen(['/root/Mimamori/hvc-p2-sample/code/faceRegister 10 0 %s' % name], shell=True)

# subprocess.call(['./camtest.py', id, name], shell=True)

