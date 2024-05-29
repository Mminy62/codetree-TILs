# 가장 작은 y값만 놓고 나머진 제거
# x값이 key, y값은 min value


n = int(input())
dic = {}

for _ in range(n):
    x, y = map(int, input().split())
    if x in dic and dic[x] > y:
        dic[x] = y
    if x not in dic:
        dic[x] = y

print(sum(dic.values()))