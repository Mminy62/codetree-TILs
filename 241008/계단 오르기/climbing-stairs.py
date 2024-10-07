'''
2 or 3

0 -> 5로 가는 방법의 
'''
from collections import deque

n = int(input())
dp = [0] * (n + 1)
q = deque([0])

while q:  
    start = q.popleft()
    if start + 2 <= n:
        dp[start + 2] += 1
        q.append(start + 2)
    if start + 3 <= n:
        dp[start + 3] += 1
        q.append(start + 3)

print(dp[n] % 10007)