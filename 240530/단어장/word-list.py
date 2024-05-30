from sortedcontainers import SortedDict

n = int(input())
sd = SortedDict()

for _ in range(n):
    word = input()
    if word in sd:
        sd[word] += 1
    else:
        sd[word] = 1

for key, value in sd.items():
    print(key, value)