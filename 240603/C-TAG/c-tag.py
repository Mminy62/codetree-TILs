'''
500 * 50 *
25000

50 자리 3개를 뽑았을때a, b의 조합이 서로 2n개 이면 가능한 것
50 50 50 
'''
from itertools import combinations

n, m = map(int, input().split())
A = []
B = []

for _ in range(n):
    A.append(input())

for _ in range(n):
    B.append(input())

answer = 0

coords = list(combinations(range(m), 3))

for i, j, k in coords:
    aset = set()
    bset = set()

    for word in A:
        aset.add(word[i] + word[j] + word[k])
    for word in B:
        bset.add(word[i] + word[j] + word[k])
    
    if len(aset) == len(aset - bset):
        answer += 1
        
print(answer)