'''
2 or 3

0 -> 5로 가는 방법의 
'''
from collections import deque

n = int(input())
dp = [0] * (n + 1)
dp[2] = 1
dp[3] = 1
for i in range(4, n + 1):
    dp[i] = dp[i - 2] + dp[i - 3]

print(dp[n] % 10007)