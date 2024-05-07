'''
N개의 집이 x = 1, x = n까지 순서대로 놓여있고, 각 Ai명의 사람이 살고 있다. 
이들은 회의를 위해 n개의 집 중 한 곳에 전부 모인다 모든 사람읭 ㅣ동거리 합이 최소인 집 선택
# 각 지점에 사는 사람들의 수

1개의 지점은 본인은 0 인덱스를 비교해야될거같음 abs(본인 - 지정 집)
'''
import sys

result = sys.maxsize

n = int(input())
home = list(map(int, input().split()))

for si in range(n):
    temp = 0
    for idx in range(n):
        if idx == si:
            continue
        distance = abs(si - idx)
        temp += home[idx] * distance
    
    result = min(temp, result)

print(result)