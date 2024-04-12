'''
타이머: 30 , 30, 30, 30(cur)
'''


'''
N*M, 
공격력이 0이하되면, 포탑이 부서지고 더이상 공격할 수 없음
k번 동안 1번 - 4가지 액션

1. 공격자 선정
0이 아닌 후보들 중 가장 약한걸 공격자로 선정
공격자 -> 가장 약한 것이므로 N + M 만큼의 공격력 상승

공격자 선정 기준
- 공격력이 가장 낮(가장 낮은 숫자)
- 2개 이상이면 가장 최근에 공격한 포탑이 가장 약한 것임(가장 최근,, 공격한 적 있는지 체크) like jump
- 그러한 포탑도 2개 이상 -> r + c가 큰걸로
- 그래도 2개 이상이면 c가 큰걸로

=> 선정되면 N + M 더해주기

2. 공격자 공격
선정된 공격자는 자신을 제외한 가장 강한 포탑을 공격

가장 강한 포탄 기준
- 공격력이 가장 높, 공격한지 가장 오래된 포탑(숫자가 낮은걸로 찾기), 행 + 열의 합이 작은 것, 열값이 작은 것

3. 공격할때
레이저 해보고 안되면 포탄 공격!

    * 공격 방법 선택 -> 공격

    (1) 레이저 공격
    - 0은 지날 수 없음(부서진 포탑)
    - 테두리를 벗어나면 반대 방향으로 나오게 된다. 
    - 공격자 위치 ~ 공격할 포탄까지 최단 경로로 공격함 -> 최단 경로가 없으면 포탄 경로 공격
    - 
    - 경로의 길이가 똑같은 최단 경로가 2개 이상이면 우/하/좌/상의 우선순위대로 먼저 움직인 경로가 선택된다. 
    - 피해자는 공격자의 파워 만큼 피해를 입는다.
    - 공격 대상을 제외한 경로에 있는 다른 포탑들도 피해를 입는다. (공격력//2 만큼)


    -> 최단 경로로 도달하는 방법: q로 넣어서 while q : => cnt 넣어서 (이동 경로를 다 알아야하는데,,)
    -> 마지막으로 도달하는 곳에 cnt가 min과 같으면 다 경로 담기 


    (2) 포탄 공격
    - 포탄을 던지는 공격
    - 공격자의 파워만큼 피해자는 피해를 입고, 주변 8개는 공격력 // 2 만큼의 피해를 입는다
    - 가장 자리에 포탄이 떨어지면, 추가 피해자가 반대편 격자에도 영향을 미친다. 



    (3) 공격 
    공격하면 공격력이 0이하가 된 포탑은 0이 된다. 

4. 포탑 정비
- 부서지지 않은 포탑 중 공격 경로에 없었고, 공격자 & 피해자가 아니었던 것들은 다 1씩 올려준다. 
# 공격자, 피해자는 알고 있고 그 경로에 있는 것도 여기까지 관리 해줘야할듯

K번
=> 종료 후 가장 강한 포탑의 공격력은?

'''
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
    small_cnt = N + M
    power = board[ax][ay]

    while q:
        record, x, y, cnt = q.popleft()

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

            if board[nx][ny] > 0:
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


# 공격자로 뽑혔는지 확인
for i in range(N):
    for j in range(M):
        if board[i][j] > 0:
            attack_cnt[(i, j)] = 0

for k in range(K):
    select_attackers(k + 1)
    select_victim()
    attack()

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
'''