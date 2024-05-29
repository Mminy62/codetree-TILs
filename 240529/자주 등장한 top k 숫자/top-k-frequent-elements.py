from collections import Counter

n, k = map(int, input().split())
arr = list(map(int, input().split()))

dic = Counter(arr)
result = []
for key, value in dic.items():
    result.append((key, value))

result.sort(key=lambda x: (-x[1], -x[0]))
for i in range(k):
    print(result[i][0], end = " ")