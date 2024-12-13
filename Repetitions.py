import sys
line = str(sys.stdin.readline().strip())
count = dict()
for letter in line:
    if letter not in count:
        count[letter] = 1
    else:
        count[letter] += 1
sys.stdout.write(str(max(count.values())))