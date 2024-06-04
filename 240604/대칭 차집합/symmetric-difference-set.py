'''
A, B
A-B, B-a
'''

n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

result = set(a - b)
result = result | set(b - a)
print(len(result))