'''
10000개를 기준으로 4방향으로 한번 
최대 돌려봤자 10000번 찍는 것
10 ** 8

원래는 10000개를 기준으로 10000개의 출구를 기준으로 매번 배열 10000개를 다 돌면서 찍는 것
10000 ** 3

=> 이럴땐 관점을 바꿔서, 출구를 기준으로 각 칸에 대한 최소 점을 구한다. 
'''
from collections import deque
INF = int(1e9)

n, h, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))


goals = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 3:
            goals.append((i, j))

# check
# 칸이 1이면 벽 
# 가중치가 다 똑같으므로 deque도 가능해 

q = deque([])
for i in range(m):
    x, y = goals[i]
    q.append((x, y, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

step = [[INF] * n for _ in range(n)]

while q:
    x, y, cnt = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        
        if arr[nx][ny] == 1:
            continue
        
        if step[nx][ny] == INF:
            step[nx][ny] = cnt + 1
            q.append((nx, ny, cnt + 1))


result = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            if step[i][j] == INF:
                result[i][j] = -1
            else: 
                result[i][j] = step[i][j]

for i in range(n):
    print(' '.join(map(str, result[i])))