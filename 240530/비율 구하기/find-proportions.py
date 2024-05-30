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
    result = format((round(value / n * 100, 4)), ".4f")
    print(f'{key} {result}')