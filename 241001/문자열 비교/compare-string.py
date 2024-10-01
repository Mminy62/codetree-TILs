'''
집합 S가 있고, 
입력으로 주어지는 m개의 문자열 중에서 집합 S에 포함되어 있는게 총 몇개인지

'''

n, m = map(int, input().split())
s1 = set()
for _ in range(n):
    s1.add(input())

s2 = set()
for _ in range(m):
    s2.add(input())

print(len(s1.intersection(s2)))