# 수가 같은 것 만큼 nC같은 수
from collections import defaultdict, Counter
from copy import deepcopy
import math

n, k = map(int, input().split())
arr = list(map(int, input().split()))
dic = defaultdict(int)
answer = 0
for v in arr:
    dic[v] += 1

for first in dic.keys():
    temp_dic = deepcopy(dic)
    temp_dic[first] -= 1
    for second in dic.keys():
        if temp_dic[second] > 0:
            temp_dic[second] -= 1
        third = k - first - second
        if third not in dic:
            continue
        if temp_dic[third] <= 0:
            continue
        
        temp = [first, second, third]
        temp = Counter(temp)
        tmp = 1
        for k, v in temp.items():
            tmp *= math.comb(dic[k], v)
        answer += tmp
        
print(answer)