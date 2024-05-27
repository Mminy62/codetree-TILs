n, m = map(int, input().split())
info = {}
for i in range(1, n + 1):
    v = input()
    info[str(i)] = v
    info[v] = str(i)

for _ in range(m):
    k = input()
    print(info[k])