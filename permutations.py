import sys
num = int(sys.stdin.readline().strip())

if num ==3 or num == 2:
    sys.stdout.write("NO SOLUTION")
else:
    odd = ""
    for i in range(1,num+1):
        if i%2:
            odd+=(str(i)+" ")
        else:
            sys.stdout.write(str(i)+" ")
    sys.stdout.write(odd)