import sys
line = str(sys.stdin.readline().strip())
res = float("-inf")
i = 0
count = 0
flag = line[0]
while i < len(line):
    while flag == line[i]:
        count += 1
        i += 1
        if i >= len(line):
            break
    if res < count:
        res = count
    count = 1
    if i >= len(line):
        break
    flag = line[i]
    i += 1
sys.stdout.write(str(res))