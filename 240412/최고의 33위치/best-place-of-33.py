'''
N * N
동전 1

'''
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

result = 0
for i in range(n - 2):
    for j in range(n - 2):
        temp = 0

        for x in range(i, i + 3):
            for y in range(j, j + 3):
                if arr[x][y]:
                    temp += 1

        
        result = max(result, temp)

print(result)