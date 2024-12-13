import sys
def main():
    num = int(sys.stdin.readline().strip())
    arr = set(map(int, sys.stdin.readline().split()))
    for i in range(1,num+1):
        if i not in arr:
            sys.stdout.write(str(i)+"\n")
            return
main()