# 가중치가 동일하면 BFS로 최단거리 구할 수 있음
from collections import deque

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# 뱀이 있는 경우 0




q = deque([(0, 0, 0)])
ex, ey = N - 1, M - 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * M for _ in range(N)]
ans = -1

while q:
    x, y, cnt = q.popleft()
    visited[x][y] = True

    if (x, y) == (ex, ey):
        ans = cnt
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if board[nx][ny] == 0:
            continue
        
        # 1 이고, 방문 안했으면 ok

        if board[nx][ny] == 1 and not visited[nx][ny]:
            q.append((nx, ny, cnt + 1))


print(ans)