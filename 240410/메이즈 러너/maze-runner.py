'''
N * N 크기의 격자
r, c 1, 1 시작
빈, 벽(1-9), 출구

- 회전 할때마다 내구도가 1씩 깍임 (벽 점수)
- 0이 빈칸
출구에 도착하면 즉시 탈출
- 1초마다 모든 참가자가 한칸씩 움직임


- 동시에 다같이 움직임
상하좌우, 벽이 없는 곳으로 이동 가능
- 출구까지 최단 거리가 가까워지는 방향으로 이동
    - 출구까지 상하좌우로 nx, ny를 비교해서 가장 가까운 방향인 곳을 선정. nx, ny로 지정, 우선순위가 동일하면 상하로 움직이는게 먼저임!(x가 변했는지 확인)
    // 방향에 따른 출구 거리 측정 -> 우선 순위도 결정해놓기(x가 바뀌는지)
    - 움직일 수 없는 상황이면 움직이지 않음// 출구 방향에 벽이 있는 경우
    - 한칸에 2명 가능 // 그냥 좌표로 가지고 있는게 낫겠다. board엔 장애물만 놔두고

- 모든 참가자 이동 -> 미로 회전
    - 한명 이상의 참가자 & 출구를 포함한 가장 작은 정사각형을 잡는다. // 각 참가자에 대해 출구랑 거리 측정, 
    - 가장 작은 정사각형이 2개 이상이면 좌 상단의 r, c가 작은게 우선
    - 시계방향 90도 회전, 회전된 벽은 내구도 1씩 깎임 // 모든 칸들이 다 회전
    => 회전때는 그럼 참가자, 출구 모두 이동, 벽들 내구도도 1씩 깎기

- K 초 동안 반반복
- 모든 참가자가 탈출하면 K초전에도 끝나기 가능
- 모든 참가자들의 이동 거리 합, 출구 좌표를 출력
'''
from copy import deepcopy
# 이동 후에 참가자 나갔는지 확인 -> dict에서 없애기

N, M, K = map(int, input().split())

board = []
people = {}

for _ in range(N):
    board.append(list(map(int, input().split())))

for num in range(M):
    r, c = map(int, input().split())
    people[num] = [r-1, c-1]
# 출구 좌표 
ex, ey = map(int, input().split())
ex -= 1
ey -= 1
board[ex][ey] = -1

# 0 빈칸, -1은 출구, 1-9는 벽

# 이동
'''
- 동시에 다같이 움직임
상하좌우, 벽이 없는 곳으로 이동 가능
- 출구까지 최단 거리가 가까워지는 방향으로 이동
    - 출구까지 상하좌우로 nx, ny를 비교해서 가장 가까운 방향인 곳을 선정. nx, ny로 지정, 우선순위가 동일하면 상하로 움직이는게 먼저임!(x가 변했는지 확인)
    // 방향에 따른 출구 거리 측정 -> 우선 순위도 결정해놓기(x가 바뀌는지)
    - 움직일 수 없는 상황이면 움직이지 않음// 출구 방향에 벽이 있는 경우
    - 한칸에 2명 가능 // 그냥 좌표로 가지고 있는게 낫겠다. board엔 장애물만 놔두고
'''
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 출구 방향을 먼저 찾기 ex, ey
# 출구 방향에 대해 아예 people 좌표 움직이기
ans = 0

def moving_direction(idx, x, y):
    global ans
    di = 5
    distance = 100

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        temp = abs(nx - ex) + abs(ny - ey)
        
        if temp == distance and di > i:
            di = i
        elif temp < distance:
            distance = temp
            di = i
        
    if di != 5:
        nx = x + dx[di]
        ny = y + dy[di]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return
        if board[nx][ny] > 0:
            return
        #움직이기 가능 
        ans += 1
        if (nx, ny) == (ex, ey):#출구로 빠져나가서 삭제하기 
            del people[idx]
            return

        people[idx] = [nx, ny]

    return 


# 정사각형 찾기 

def find_smallsquare():
    size = 0
    moving_person = []
    for size in range(2, N + 1):
        for x1 in range(N - size + 1):
            for y1 in range(N - size + 1):
                # i + size
                x2 = x1 + size - 1
                y2 = y1 + size - 1
                
                # 출구가 포함되지 않는 경우 패스 
                if x1 > ex or ex > x2 or y1 > ey or ey > y2:
                    continue
                
                # 출구 포함 되었으면, 참가자 있는지 확인 
                for key, (px, py) in people.items():
                    if x1 <= px and px <= x2 and y1 <= py and py <= y2:
                        moving_person.append(key)
                        # 찾음
                if moving_person:
                    return (x1, y1, size, moving_person)

    return (0, 0, 0, [])

def rotate():
    global ex, ey
    x1, y1, size, moving_person = find_smallsquare()

    origin = deepcopy([board[i][y1: y1 + size] for i in range(x1, x1 + size)])
    temp = [[0] * size for _ in range(size)]

    # 사람 넣기 
    for key in moving_person:
        r, c = people[key]
        if type(origin[r - x1][c - y1]) != list:
            origin[r - x1][c - y1] = [10 + key]
        else:
            origin[r - x1][c - y1].append(10 + key)


    # # x1~size 까지의 행결 시계방향 90도 돌리기  
    for i in range(size):
        for j in range(size):
            temp[j][size - i - 1] = origin[i][j]

    # 돌린 후 집어 넣기 
    for i in range(x1, x1 + size):
        for j in range(y1, y1 + size):
            value = temp[i - x1][j - y1]
            if type(value) == list:
                for key in value:
                    people[key - 10] = [i, j]
                    board[i][j] = 0
                continue

            else:#일반 정수 값인 경우 
                if value == -1:
                    ex, ey = i, j

                if value > 0:
                    value -= 1

            board[i][j] = value
    
    return 


for i in range(K):
    people_copy = people.copy()
    # 움직이기 
    for key, (x, y) in people_copy.items():
        moving_direction(key, x, y)

    # 이동 후에 people 없으면 게임 종료 -> 시간 반복문 나가기 
    if not people.keys():
        break

    rotate()

print(ans)
print(ex + 1, ey + 1)

'''
5 3 8
0 8 0 0 1
0 1 0 0 0
0 1 0 1 0
0 0 0 1 0
0 0 0 0 0
3 3
1 1
3 5
3 1
'''