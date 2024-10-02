from bisect import bisect_left
N, K = map(int, input().split())
pre = list(map(int, input().split()))
coords = list(range(1, N + 1))

for num in pre:
    coords.remove(num)

after = [0] * K
length = len(coords)
flag = False

for i in range(K - 1, -1, -1):
    if flag:
        after[i] = pre[i]
        continue
    index = bisect_left(coords, pre[i])
    if index == length:
        after[i] = pre[i]
        continue
    else:
        after[i] = coords[index]
        flag = True

if after == pre:
    print("NONE")
else:
    print(" ".join(map(str, after)))