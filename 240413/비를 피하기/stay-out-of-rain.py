'''
n * n
h명

가장 가까운 곳까지의 거리
0으론 이동 가능 1은 벽, 2까지 가능
3이 도착지
상하좌우


'''
from collections import deque


n, h, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 2인 곳부터 가장 가까운 3인 곳까지의 거리를 찾는 것
# 3인 곳의 위치 받아두고, 그 위치까지의 큐 해보기 ex, ey가 m번 반복되는 것

goals = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 3:
            goals.append((i, j))



# check
def check(sx, sy):
    ans = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(m):
        ex, ey = goals[i]

        q = deque([])
        q.append((sx, sy, 0))
        visited = [[False] * n for _ in range(n)]
        visited[sx][sy] = True

        while q:
            x, y, cnt = q.popleft()
            # 넘어가면 안되고, 1이면 안되고
            # 2이거나 0
            # 가중치가 똑같으니까, 먼저 도착한게 먼저지 않나?
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny] == 1:
                    continue
                if (nx, ny) == (ex, ey):
                    ans.append(cnt + 1)
                    break

                if not visited[nx][ny]:
                    q.append((nx, ny, cnt + 1))
                    visited[nx][ny] = True


    if not ans:
        return -1
    else:
        return min(ans)

result = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            result[i][j] = check(i, j)

for i in range(n):
    print(' '.join(map(str, result[i])))