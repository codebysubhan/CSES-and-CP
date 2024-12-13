import sys

num = int(sys.stdin.readline().strip())

sys.stdout.write(str(num) + " ")
while num != 1:
    if num%2:
        num*=3
        num+=1
    else:
        num>>=1
    sys.stdout.write(str(num) + " ")

