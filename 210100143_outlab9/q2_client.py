import xmlrpc.client
import sys

num = int(sys.argv[1])

s = xmlrpc.client.ServerProxy('http://localhost:8080')
print(s.getMagicNumber(num))
s.kill()
