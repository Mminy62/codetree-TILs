'''

3 6 2 6 7 7 2
우선순위 큐 -> O(NlogN)

'''
import heapq

pq = []
n, m = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(n):
    heapq.heappush(pq, -arr[i])

for _ in range(m):
    num = heapq.heappop(pq)
    heapq.heappush(pq, num + 1)

print(-heapq.heappop(pq))