#!/usr/bin/python3

res=''
for i, val in enumerate(range(ord('z'), ord('a') - 1, -1), start = 1):
    if(i % 2 == 0):
        res += chr(val - 32)
    else:
        res += chr(val)
print("{:s}".format(res), end="")
