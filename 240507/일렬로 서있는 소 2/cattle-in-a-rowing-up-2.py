'''
서로 다른 3개의 숫자만 두배로 해서 인접한 숫자간의 차이 합이 최대
'''

# 위치가 i < j < k
n = int(input())
arr = list(map(int, input().split()))
comb = []
answer = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            comb.append((i, j, k))

for i, j, k in comb:
    if arr[i] <= arr[j] and arr[j] <= arr[k]:
        answer += 1

print(answer)