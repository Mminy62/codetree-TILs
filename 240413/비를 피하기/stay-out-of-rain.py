'''
n * n
h명

가장 가까운 곳까지의 거리
0으론 이동 가능 1은 벽, 2까지 가능
3이 도착지
상하좌우


'''
import heapq
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
def check(sx, sy):
    ans = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for k in range(m):
        ex, ey = goals[k]
        q = []
        heapq.heappush(q, (0, sx, sy))
        visited = [[False] * n for _ in range(n)]
        visited[sx][sy] = True
        distance = [[INF] * n for _ in range(n)]
        distance[sx][sy] = 0

        while q:
            cnt, x, y = heapq.heappop(q)
            # 넘어가면 안되고, 1이면 안되고, 2/0 이면 통과 가능

            if cnt > distance[x][y]:
                continue

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if arr[nx][ny] == 1:
                    continue

                if (nx, ny) == (ex, ey):
                    ans.append(cnt + 1)
                    break

                if not visited[nx][ny]:
                    if cnt + 1 < distance[nx][ny]:
                        distance[nx][ny] = cnt + 1
                        heapq.heappush(q, (cnt + 1, nx, ny))
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