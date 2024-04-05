n, m, k, c = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

rx = [-1, -1, 1, 1]
ry = [-1, 1, 1, -1]

years = [[0] * n for _ in range(n)]

# 성장
def growth():
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                cnt = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if board[nx][ny] > 0:
                        cnt += 1
                board[i][j] += cnt

# 번식
def breeding():
    breed = []
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                cnt = 0
                pos = []
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if board[nx][ny] == 0 and years[nx][ny] == 0:
                        cnt += 1
                        pos.append((nx, ny))

                if cnt:
                    for x, y in pos:
                        breed.append((x, y, board[i][j] // cnt))

    for x, y, cnt in breed:
        board[x][y] += cnt

# 제초제
def removing():
    max_cnt = 0
    max_pos = (n, n)

    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:  # 제초제 작업 시작
                cnt = board[i][j]
                for d in range(4):
                    x, y = i, j
                    for _ in range(k):
                        nx = x + rx[d]
                        ny = y + ry[d]

                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            break
                        if board[nx][ny] <= 0:# 비어있거나, 벽이거나
                            break

                        if board[nx][ny] > 0:
                            cnt += board[nx][ny]
                        x, y = nx, ny

                if max_cnt < cnt:
                    max_pos = (i, j)
                    max_cnt = cnt
                elif max_cnt == cnt and max_pos > (i, j):
                    max_pos = (i, j)

    # 최대 제초제 위치에서 제초제 뿌리기
    # print(max_pos, max_cnt)

    if max_pos != (n, n):
        mx, my = max_pos
        board[mx][my] = 0
        years[mx][my] = c

        for d in range(4):
            x, y = max_pos
            for _ in range(k):
                nx = x + rx[d]
                ny = y + ry[d]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break
                if board[nx][ny] == 0:
                    years[nx][ny] = c
                    break

                if board[nx][ny] < 0:# -1 벽
                    break
                # 나무가 있다면
                years[nx][ny] = c
                board[nx][ny] = 0
                x, y = nx, ny

    return max_cnt


ans = 0
for year in range(m):

    growth()
    breeding()

    for i in range(n):
        for j in range(n):
            if years[i][j] > 0:
                years[i][j] -= 1

    ans += removing()

print(ans)