import heapq
from collections import deque

N, M, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

#포탑의 좌표를 기준으로 확인
attack_cnt = {}
ax, ay = 0, 0 #공격자
vx, vy = 0, 0 # 피해자

# 1. 공격자 선정
def select_attackers(turn):
    global ax, ay
    attackers = []
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                heapq.heappush(attackers, (board[i][j], -attack_cnt[(i, j)], -(i + j), -j, (i, j)))

    attacker = heapq.heappop(attackers)
    ax, ay = attacker[-1]

    # 공격자에 공격력 더하기
    board[ax][ay] += (N + M)
    # 최근 공격했는지의 기록 관리
    attack_cnt[(ax, ay)] = turn

    return


# 2. 피해자 고르기
# 가장 강한 포탄 고르기
# ax, ay가 아닌 걸로
def select_victim():
    global vx, vy

    victims = []
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and (i, j) != (ax, ay):
                heapq.heappush(victims, (-board[i][j], attack_cnt[(i, j)], (i + j), j, (i, j)))

    victim = heapq.heappop(victims)
    vx, vy = victim[-1]
    return

# 넘어가는 범위 좌표 관리
def bound_square(nx, ny):
    if nx < 0:
        nx = N - abs(nx)
    if nx >= N:
        nx = nx - N
    if ny < 0:
        ny = M - abs(ny)
    if ny >= M:
        ny = ny - M

    return (nx, ny)


# 3. 공격 경로 + 공격 진행 + 포탄 정비

def attack():
    q = deque([]) # 기록 관리, 현재 좌표, cnt
    move_cnt = 0
    q.append(([], ax, ay, move_cnt))

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    smallest_route = [] # count, [records] 로 정렬하면 알아서 뽑도록
    small_cnt = 18
    power = board[ax][ay]

    visited = [[False] * M for _ in range(N)]
    visited[vx][vy] = True
    visited[ax][ay] = True

    while q:
        record, x, y, cnt = q.popleft()
        visited[x][y] = True

        if cnt + 1 > small_cnt:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                nx, ny = bound_square(nx, ny)
                # 이 넘은게 vx, vy일 수도 있음

            if board[nx][ny] == 0:
                continue

            if (nx, ny) == (vx, vy) and small_cnt >= cnt + 1:
                smallest_route.append((cnt + 1, record + [i]))
                small_cnt = cnt + 1
                continue

            if (nx, ny) != (ax, ay) and not visited[nx][ny] and board[nx][ny] > 0 :
                q.append((record + [i], nx, ny, cnt + 1))


    # 공격 진행
    # 공격 경로에도 없고, 아무 상관 없는걸 알기 위해
    visited = [[False] * M for _ in range(N)]
    visited[vx][vy] = True
    visited[ax][ay] = True

    # (1) 레이저 공격
    if smallest_route:
        smallest_route.sort()
        cnt, records = smallest_route[0]
        x, y = ax, ay

        for di in records:
            nx = x + dx[di]
            ny = y + dy[di]
            # 이때 nx, ny면 또 바꿔주기

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                nx, ny = bound_square(nx, ny)

            if (nx, ny) != (vx, vy):# 피해자가 아닌 경로인 경우
                board[nx][ny] -= (power // 2)
                visited[nx][ny] = True

            if (nx, ny) == (vx, vy):
                board[nx][ny] -= power

            if board[nx][ny] < 0:
                board[nx][ny] = 0

            x, y = nx, ny

    else:
        #포탄 공격!
        rx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        ry = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
        # 아예 vx, vy면 power 로 삭제

        x, y = vx, vy
        for i in range(9):
            nx = x + rx[i]
            ny = y + ry[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                nx, ny = bound_square(nx, ny)

            # 벽이거나 공격자인 경우 제외
            if board[nx][ny] == 0 or (nx, ny) == (ax, ay):
                continue

            if board[nx][ny] > 0:
                if (nx, ny) == (vx, vy):
                    board[nx][ny] -= power
                else:
                    board[nx][ny] -= (power // 2)
                    visited[nx][ny] = True

            if board[nx][ny] < 0:
                board[nx][ny] = 0

    # 4. 포탄 정비
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and not visited[i][j]:
                board[i][j] += 1

    return

def final_check():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                cnt += 1
    if cnt == 1:
        return True
    return False


# 공격자로 뽑혔는지 확인
for i in range(N):
    for j in range(M):
        if board[i][j] > 0:
            attack_cnt[(i, j)] = 0


for k in range(K):
    select_attackers(k + 1)
    select_victim()
    attack()
    if final_check():
        break



ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] > 0:
            ans = max(ans, board[i][j])

print(ans)



'''
4 5 1
5 1 4 8 26
8 0 10 8 13
8 0 11 8 8
0 0 0 8 0

5 4 5
9 0 4 7
5 4 4 4
2 1 0 3
3 3 0 0
2 7 8 10

'''