N, K = map(int, input().split())
arr = [0] * (N + 1)
for _ in range(K):
    a, b = map(int, input().split())
    arr[a] += 1
    arr[b + 1] -= 1

for i in range(1, N + 1):
    arr[i] += arr[i - 1]
arr.sort()
print(arr[N//2])