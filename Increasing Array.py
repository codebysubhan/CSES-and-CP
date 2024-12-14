import sys
num = int(sys.stdin.readline().strip())
arr = map(int, sys.stdin.readline().split())
flag = float("-inf")
count = 0
for i in arr:
    if flag <= i:
        flag = i
    else:
        count += (flag - i)
sys.stdout.write(str(count))