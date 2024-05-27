'''
6개의 문자열이 주어진 뒤에 끝에 k가 주어졌을 때, 
문자열 k가 몇번째로 주어졌는지를 판단

'''
from collections import Counter
arr = []
n = int(input())

for _ in range(n):
    arr.append(input())

temp = Counter(arr)

print(max(temp.values()))