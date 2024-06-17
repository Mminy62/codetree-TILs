'''
(1, 7), (3, 2), (3, )
'''
import heapq
n, m = map(int, input().split())
q = []
for _ in range(n):
    x, y = map(int, input().split())
    heapq.heappush(q, (abs(x) + abs(y), x, y))

for _ in range(m):
    res, x, y = heapq.heappop(q)
    heapq.heappush(q, (res + 4, x + 2, y + 2))

item = heapq.heappop(q)
print(item[1], item[2])