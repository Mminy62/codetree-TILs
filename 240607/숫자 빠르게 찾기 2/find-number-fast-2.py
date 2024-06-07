# -x보다 같거나 최소 숫자를 출력한다 -> bisect_left
from sortedcontainers import SortedSet

n, m = map(int, input().split())

arr = list(map(int, input().split()))
s = SortedSet(arr)

for _ in range(m):
    num = int(input())
    idx = s.bisect_left(num)
    if idx == n:
        print(-1)
    else:
        print(s[idx])