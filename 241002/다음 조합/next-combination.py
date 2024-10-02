from bisect import bisect_left
N, K = map(int, input().split())
pre = list(map(int, input().split()))
coords = list(range(1, N + 1))

for num in pre:
    coords.remove(num)
coords.sort()

after = [0] * K
length = len(coords)
flag = False

for i in range(K - 1, 0, -1):
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

if not flag: #맨 앞자리까지 변화X
    if pre[0] == N - (K - 1):
        print("NONE")
    else:
        after = range(pre[0] + 1, pre[0] + K)
        print(" ".join(map(str, after)))
else:
    after[0] = pre[0]
    print(" ".join(map(str, after)))