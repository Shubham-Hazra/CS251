import os
import sys
import subprocess

ip = sys.argv[1]
command = "ping -c 5 -q -w 5 " + ip+">out.txt"
remove_command = "rm -rf out.txt"
out = os.system(command)
os.system(remove_command)
if out == 0:
    print("YES")
else:
    print("NO")