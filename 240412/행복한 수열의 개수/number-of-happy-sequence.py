'''
행 기준으로만 완탐하면 될듯

'''

# 수열을 합쳐서 정렬 시키면 -> m개씩 맞아 떨어지는지 확인
from copy import deepcopy
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

ans = 0
# 먼저 행검사 
for i in range(n):
    temp = arr[i]
    pre = temp[0]
    cnt = 1
    for j in range(1, n):
        if pre == temp[j]:
            cnt += 1
        else:
            cnt = 1

        pre = temp[j]

    if cnt >= m:
        ans += 1

for i in range(n):
    temp = []
    for j in range(n):
        temp.append(arr[j][i])

    pre = temp[0]
    cnt = 1
    for j in range(1, n):
        if pre == temp[j]:
            cnt += 1
        else:
            cnt = 1

        pre = temp[j]     
        
    if cnt >= m:
        ans += 1

    
print(ans)