'''
서로다른 n개의 점
m개의 질의가 있는데
각 질의마다 한개의 숫자 k
k보다 x값이 같거나 큰거, bisect_left
x값이 가장 작은 점을 찾아 지운다. 

'''
from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

s = SortedSet(arr)

for _ in range(m):
    num = int(input())
    idx = s.bisect_left((num, 0))
    if idx == len(s):
        print(-1, -1)
    else:
        print(s[idx][0], s[idx][1])
        s.remove(s[idx])