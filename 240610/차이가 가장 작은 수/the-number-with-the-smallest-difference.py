'''
n개의 정수로 이루어진 수열에서 두 수를 골랐을 때 
그 
'''
import sys
from sortedcontainers import SortedSet
s = SortedSet()
n, m = map(int, input().split())
for _ in range(n):
    s.add(int(input()))

ans = sys.maxsize
for i in range(n):
    num = s[i]
    idx = s.bisect_left(num + m)
    if idx == len(s):
        continue
    ans = min(ans, s[idx] - num)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)