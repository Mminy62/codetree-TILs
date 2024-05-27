from collections import Counter
n, m = map(int, input().split())
arr = list(map(int, input().split()))
temp = Counter(arr)
cmds = list(map(int, input().split()))

for cmd in cmds:
    print(temp[cmd], end = " ")