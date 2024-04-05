'''
* 벽, 나무, 제초제 있음 
성장은 모든 나무가 동시에 이루어짐
인접한 칸에 나무가 있는 개수만큼 커짐

- 번식
    - 나무는 인접한 4개의 칸 중 비어있는 칸에 번식
    - 나무 // 비어있는 칸의 수 만큼 한칸에 나무가 번식된다.
    - 모든 나무가 동시에 일어남. 빈칸이 겹칠 수 있음. 
    - 더할 거를 (위치, 개수) 해가지구 번식이 모두 다 끝나면 더해야함

- 제초제(-로 표시, +1 씩 해가지구 )
    - 나무가 있는 칸에 제초제를 뿌려야 효과 ㅇ , 빈 곳엔 0
    - 그 칸 기준 4개 대각선 방향으로 k칸 만큼 전파.
    - 전파 도중 나무가 없거나/ 벽인 경우 그 칸까지만 제초제가 뿌려지고, 이후 칸엔 안뿌려짐
    - 제초제 뿌려진 칸엔 C년 동안 유지 , c+1엔 사라짐
    - 그 곳에 다시 뿌려지면 C로 다시 업데이트
    +> -1씩 해야되나,, m년이니까 맞는듯 1000번

    => 가장 많은 나무를 죽일 수 있는 곳에 제초제 뿌리기
    - 각 칸을 돌면서 세고, 가장 많은 곳의 위치, 갯수 갖고 있기
    - 중복-> 행, 열이 작은 순으로 정렬 순!

- 매년 제초제가 남아있는지 확인, -1 씩 줄이기

'''

n, m, k, c = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if board[i][j] == -1:
            board[i][j] = -20

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

rx = [-1, -1, 1, 1]
ry = [-1, 1, 1, -1]

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
                    if board[nx][ny] == 0:
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
            if board[i][j] > 0:#제초제 작업 시작
                cnt = board[i][j]
                for d in range(4):
                    x, y = i, j
                    for _ in range(k):
                        nx = x + rx[d]
                        ny = y + ry[d]

                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            break
                        if board[nx][ny] == 0 or board[nx][ny] == -20:
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
    if max_pos != (n, n):
        mx, my = max_pos
        board[mx][my] = -c
        for d in range(4):
            x, y = max_pos
            for _ in range(k):
                nx = x + rx[d]
                ny = y + ry[d]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break
                if board[nx][ny] == 0:
                    board[nx][ny] = -c
                    break
                if board[nx][ny] == -20:
                    break
                
                board[nx][ny] = -c
                x, y = nx, ny

    return max_cnt


ans = 0
for year in range(m):
    growth()
    breeding()
    ans += removing()

    if year != 0:
        for i in range(n):
            for j in range(n):
                if board[i][j] < 0 and board[i][j] != -20:
                    board[i][j] += 1



print(ans)