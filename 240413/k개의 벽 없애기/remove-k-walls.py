'''
k개 완탐
1이 벽임
1에서부터 시작해서 
'''
import math
from itertools import combinations
from collections import deque
from copy import deepcopy

INF = int(1e9)

ans = INF
board = []
n, k = map(int, input().split())
for _ in range(n):
    board.append(list(map(int, input().split())))

sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
sx, sy = sx - 1, sy - 1
ex, ey = ex - 1, ey - 1


# 벽의 좌표를 기준으로 combination with k
# 각각의 벽을 제거해보고, 시작부터 끝까지 도착하는 최닫ㄴ 거리를 측정, 
# 10000 * 70개 , popleft로 해결 가능 (가중치 1이니까), visited로만 하고, ex, ey에 도착했을때의 result를 넣어놓는다. 
# ans가 계속 INF이면 -1로 출력

# 벽 좌표들에 대한 combination 생성
walls = []

for i in range(n):
    for j in range(n):
        if board[i][j]:
            walls.append((i, j))

walls_comb = list(combinations(walls, k))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for wall_list in walls_comb:

    cboard = deepcopy(board)
    visited = [[False] * n for _ in range(n)]

    for wx, wy in wall_list:
        cboard[wx][wy] = 0
    
    q = deque([(sx, sy, 0)])
    visited[sx][sy] = True

    while q:
        x, y, cnt = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if cboard[nx][ny] == 1:
                continue
            
            if (nx, ny) == (ex, ey):
                if ans > cnt + 1:
                    ans = cnt + 1
                break

            if not visited[nx][ny]:
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = True
    

if ans == INF:
    ans = -1

print(ans)