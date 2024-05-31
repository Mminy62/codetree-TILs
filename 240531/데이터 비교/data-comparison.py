n = int(input())
arr1 = set(list(map(int, input().split())))
n2 = int(input())
arr2 = list(map(int, input().split()))
result = []
for i in range(n2):
    if arr2[i] in arr1:
        result.append(1)
    else:
        result.append(0)

for item in result:
    print(item, end = " ")