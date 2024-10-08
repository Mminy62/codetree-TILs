n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 2

if n > 1:
    for i in range(2, n + 1):
        dp[i] = 2 * dp[i - 1] + 3 * dp[i - 2]
        if i >= 3:
            dp[i] += 2 * (sum(dp[0:i - 3 + 1]))

print(dp[n] % 1000000007)