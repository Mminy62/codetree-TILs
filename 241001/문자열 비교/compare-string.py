'''
집합 S가 있고, 
입력으로 주어지는 m개의 문자열 중에서 집합 S에 포함되어 있는게 총 몇개인지

'''
from collections import defaultdict
n, m = map(int, input().split())
s1 = set()
for _ in range(n):
    s1.add(input())

sdict = defaultdict(int)
for _ in range(m):
    sdict[input()] += 1
s2 = set(sdict.keys())
keys = s1.intersection(s2)

result = 0
for key in keys:
    result += sdict[key]

print(result)