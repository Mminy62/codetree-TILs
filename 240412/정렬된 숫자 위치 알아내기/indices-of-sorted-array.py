'''
N인 수열
오름차순 정렬

'''
from bisect import bisect_left
n = int(input())
origin = list(map(int, input().split()))
temp = sorted(origin)

result = {}
for i in range(n):
    key, value = temp[i], i + 1
    if key not in result.keys():
        result[key] = [value]
    else:
        result[key].append(value)

for i in range(n):
    key = origin[i]
    print(result[key].pop(0), end = " ")