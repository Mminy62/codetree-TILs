N, M = map(int, input().split())

# chr(65)
arr = [[0] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

di = 0
x, y = 0, -1
nx, ny = 0, 0

for alpha in range(65, 65 + N * M):

    while True:
        nx, ny = x + dx[di], y + dy[di]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            di = (di + 1) % 4
            continue
        if arr[nx][ny] != 0:
            di = (di + 1) % 4
            continue
        break

    arr[nx][ny] = chr(alpha)
    x, y = nx, ny


for i in range(N):
    print(' '.join(arr[i]))