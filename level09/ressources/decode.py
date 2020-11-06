import sys

code = sys.argv[1]
decode=""

a=0
for i in code:
        decode += chr(ord(i)-a)
        a+=1


print(decode)