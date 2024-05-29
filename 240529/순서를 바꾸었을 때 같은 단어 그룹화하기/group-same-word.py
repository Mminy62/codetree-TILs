from collections import defaultdict

n = int(input())
dic = defaultdict(int)

for _ in range(n):
    temp = ''.join(sorted(input()))
    dic[temp] += 1

print(max(dic.values()))