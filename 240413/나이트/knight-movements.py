import heapq
INF = int(1e9)

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

n = int(input())
sx, sy, ex, ey = map(int, input().split())
sx -= 1
sy -= 1
ex -= 1
ey -= 1

ans = -1

q = []
# 시작 위치, 벙문 했던 곳은 가지 않는다. 먼저 방문하면 장땡임 
heapq.heappush(q, (0, sx, sy))
distance = [[INF] * n for _ in range(n)]

while q:
    cnt, x, y = heapq.heappop(q)

    if distance[x][y] < cnt:
        continue

    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        
        if cnt + 1 < distance[nx][ny]:
            distance[nx][ny] = cnt + 1
            heapq.heappush(q, (cnt + 1, nx, ny))


print(distance[ex][ey])