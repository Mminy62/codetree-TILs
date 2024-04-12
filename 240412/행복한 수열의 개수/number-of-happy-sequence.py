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

def check(seq):
    max_cnt, cnt = 1, 1
    for i in range(1, n):
        if seq[i - 1] == seq[i]:
            cnt += 1
        else:
            cnt = 1
        max_cnt = max(max_cnt, cnt)

    if max_cnt >= m:
        return True
    return False

# 먼저 행검사 
for i in range(n):
    temp = arr[i]
    if check(temp):
        ans += 1

for i in range(n):
    temp = []
    for j in range(n):
        temp.append(arr[j][i])

    if check(temp):
        ans += 1    
    
print(ans)