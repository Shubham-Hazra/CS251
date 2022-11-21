out  = open('out.txt','r')

d = {}

for line in out.readlines():
    l = line.split()
    d[l[0]] = l[1]

out1 = open('out1.txt','r')

different = False

for line in out1.readlines():
    l1 = line.split()
    if(d[l1[0]] != l1[1]):
        print("Different")
        different = True
        break

if not different:
    print("Same")
