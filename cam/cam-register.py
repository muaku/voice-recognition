import os
import sys
import subprocess

argv = sys.argv
id = int(sys.argv[1])
name = sys.argv[2]
subprocess.Popen(['/root/Mimamori/hvc-p2-sample/code/faceRegister.out %d 0 %s' % (id,name)], shell=True)

#p = subprocess.Popen(['exec /root/Mimamori/hvc-p2-sample/code/faceRegister.out %d 0 %s' % (id,name)], stdout=subprocess.PIPE, shell=True)
#p.kill()