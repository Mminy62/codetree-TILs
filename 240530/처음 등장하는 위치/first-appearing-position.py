# 오름차순 정렬이 들어간 dict를 뽑아내고 싶을 때 사용하는 듯
from sortedcontainers import SortedDict

n = int(input())
arr = list(map(int, input().split()))
sd = SortedDict()

for i, v in enumerate(arr):
    if v in sd:
        continue
    else:
        sd[v] = i + 1

for key, value in sd.items():
    print(key, value)