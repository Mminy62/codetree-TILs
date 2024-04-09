n = int(input())
arr = list(map(int, input().split()))
result = []

for i in range(n):
    if (i + 1) % 2:
        temp = sorted(arr[:i + 1])
        result.append(temp[(i + 1) // 2])

print(' '.join(map(str, result)))