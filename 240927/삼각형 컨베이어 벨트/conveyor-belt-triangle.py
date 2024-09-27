n, t = map(int, input().split())
arr = []
for _ in range(3):
    arr += list(map(int, input().split()))

t = t % len(arr)
arr = arr[-t:] + arr[:-t]

for i in range(3):
    print(" ".join(map(str, arr[i * n: i * n + n])))