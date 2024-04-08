N, M = map(int, input().split())
arr = [[1] * M for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
num = 1
x, y = -1, -1
N -= 1
M -= 1


while N >= 0 and M >= 0:
    x += 1
    y += 1
    for i in range(4):
        if i % 2 == 0:
            time = M
        else:
            time = N
        for k in range(time):
            if arr[x][y] == 1:
                arr[x][y] = num
            nx, ny = x + dx[i], y + dy[i]
            num += 1
            x, y = nx, ny

    N -= 2
    M -= 2

for i in range(len(arr)):
    print(' '.join(map(str, arr[i])))