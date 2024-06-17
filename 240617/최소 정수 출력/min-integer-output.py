'''

'''
import heapq
n = int(input())
q = []
for _ in range(n):
    cmd = int(input())
    if not cmd:
        if not q:
            print(0)
        else:
            item = heapq.heappop(q)
            print(item)
    else:
        heapq.heappush(q, cmd)