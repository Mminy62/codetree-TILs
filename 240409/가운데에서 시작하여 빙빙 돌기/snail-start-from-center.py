n = int(input())

arr = [[0] * n for _ in range(n)]

x, y = n // 2, n // 2

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
di = 0
cnt = 0
time = 1
num = 1
flag = False

while True:
    if cnt == 2:
        time += 1
        cnt = 0
    
    for _ in range(time):
        if x < 0 or x >= n or y < 0 or y >= n:
            flag = True
            break

        arr[x][y] = num
        nx = x + dx[di]
        ny = y + dy[di]
        x, y = nx, ny
        num += 1
    
    di = (di + 1) % 4
    cnt += 1

    if flag:
        break
    
for i in range(n):
    print(' '.join(map(str, arr[i])))