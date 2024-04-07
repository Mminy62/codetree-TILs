from collections import deque
from copy import deepcopy
knight_pos = {}

q = deque([])
# 칸 수, 기사 수, 명령 수
L, N, Q = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = [[2] * (L + 2)]

for _ in range(L):
    temp = [2] + list(map(int, input().split())) + [2]
    board.append(temp)

board.append([2] * (L + 2))

# 함정과 벽은 안없어지니까 board는 유지
power = {}

for num in range(1, N + 1):
    r, c, h, w, k = map(int, input().split())
    power[num] = k
    knight_pos[num] = [r, c, h, w, k]

cmds = []
for _ in range(Q):
    cmds.append(tuple(map(int, input().split())))

moving_num = []

def search_moving_knight(nx, ny): # 해당 번호 보내기 30 * 40 * 40
    keys = knight_pos.keys()
    for key in keys:
        r, c, h, w, k = knight_pos[key]
        for i in range(r, r + h):
            for j in range(c, c + w):
                if (i, j) == (nx, ny):
                    return key
    return 0
ans = 0
# 실제 명령어
for a, direct in cmds:
    # 명령 받을 기사가 없으면 무시
    if a not in knight_pos.keys():
        continue

    moving_num = [a]
    q = deque([knight_pos[a]])
    flag = False
    # 이동할 방향에 대해, 같이 이동할 기사번호 찾기
    while q and not flag:
        r, c, h, w, k = q.popleft()
        # 검사할 좌표가 방향에 따라 달라
        if direct == 0:
            r1, r2 = r, r + 1
            c1, c2 = c, c + w
        elif direct == 1:
            r1, r2 = r, r + h
            c1, c2 = c + w - 1, c + w
        elif direct == 2:
            r1, r2 = r + h - 1, r + h
            c1, c2 = c, c + w
        else:
            r1, r2 = r, r + h
            c1, c2 = c, c + 1

        for i in range(r1, r2):
            for j in range(c1, c2):
                nx = i + dx[direct]
                ny = j + dy[direct]

                if nx < 1 or nx > L or ny < 1 or ny > L or board[nx][ny] == 2:  # 끝이 벽이거나 벽에 부딪힌 경우 아무도 못움직임
                    moving_num = []
                    flag = True
                    break

                if flag:
                    break
                # 아니면 knight_pos 기준으로 nx, ny에 기사가 있는지 찾고 그 번호를 moving_num에 저장
                knum = search_moving_knight(nx, ny)
                if knum and knum not in moving_num:
                    moving_num.append(knum)
                    q.append(knight_pos[knum])

    # 움직이는 기사 번호 뽑았으면 기사 이동
    # knight_pos 안에서의 r, c 값 바꾸기
    for idx in moving_num:
        knight_pos[idx][0] += dx[direct]
        knight_pos[idx][1] += dy[direct]

    # 기사 데미지 측정
    for key in moving_num:
        if key == a:
            continue

        r, c, h, w, k = knight_pos[key]
        for i in range(r, r + h):
            for j in range(c, c + w):
                if board[i][j] == 1 and power[key] > 0:
                    power[key] -= 1

    # 파워가 없으면 지우기
    temp = power.copy().keys()
    for key in temp:
        if power[key] <= 0:
            del power[key]
            del knight_pos[key]

    # 살아있는 생존에서 K - power 하는게 나을듯

for key, value in knight_pos.items():
    ans += (value[-1] - power[key])

print(ans)