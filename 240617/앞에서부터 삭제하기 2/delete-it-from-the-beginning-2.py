'''
'''
import heapq

n = int(input())
arr = list(map(int, input().split()))
q = []
for i in range(n):
    heapq.heappush(q, arr[i])

res = 0
for i in range(n - 2):
    item = arr[i]
    q.remove(item)
    min_num = heapq.heappop(q)

    res = max(res, sum(q) / len(q))
    heapq.heappush(q, min_num)

print(format(res, ".2f"))