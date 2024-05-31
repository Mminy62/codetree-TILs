# 각 자리에 앉는 것들을 set으로 놓고 
# 
from collections import defaultdict

n, k = map(int, input().split())
move = []
for _ in range(k):
    move.append(tuple(map(int, input().split())))

arr = [i for i in range(1, n + 1)]
dic = defaultdict(set)
for i in range(1, n + 1):
    dic[i].add(i - 1)

for i in range(3 * k):
    i %= k
    a, b = move[i]
    a, b = a - 1, b - 1
    arr[a], arr[b] = arr[b], arr[a]
    dic[arr[a]].add(b)
    dic[arr[b]].add(a)

for i in range(1, n + 1):
    print(len(dic[i]))