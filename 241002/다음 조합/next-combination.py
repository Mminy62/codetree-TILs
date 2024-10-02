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

for i in range(K - 1, -1, -1):
    if flag:
        after[i] = pre[i]
        continue
    index = bisect_left(coords, pre[i])
    if index == length:
        after[i] = pre[i]
        continue
    if not flag and i == 0:
        # 앞자리까지왔다는 뜻 -> 
        if pre[i] == N - (K - 1):
            after = "NONE"
        else:
            after = range(pre[i] + 1, pre[i] + 4)
    else:
        after[i] = coords[index]
        flag = True


print(" ".join(map(str, after)))