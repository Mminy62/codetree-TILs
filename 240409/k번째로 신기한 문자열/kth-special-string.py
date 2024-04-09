n, k, T = input().split()
n = int(n)
k = int(k)
result = []
length = len(T)
for _ in range(n):
    temp = input()
    if temp[:length] == T:
        result.append(temp)

result.sort()
print(result[k-1])