'''
격자 밖으로 나가서는 안됨
지나가는 합이 최대가 되도록
- 사이즈가 크다고 다 좋은 것도 아님
- 마주보는 길이가 같아야 직사각형이 만들어짐
현재 지점에서 길이가 1, ~ 끝에 벽에 닿을때까지 한번 해보기 (최대 x만큼 해보기)
가로 길이에 대해, 세로 길이도 1~ 벽에 닿을때까지 더해보기 (현재 자리의 x만큼 해보기)
step1, step2
dx = [-1, -1, 1, 1]
dy = [1, -1, -1, 1]
벽을 넘어가는 길이면, 

# 최초 시작 자리(2, 1)
# 끝나는 자리 (n-1, n-2)
sta
'''

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, -1, 1, 1]
dy = [1, -1, -1, 1]

def in_range(step1, step2, x, y):
    cx, cy = x, y
    # if x == 3 and y == 1:
    #     print(x, y, step1, step2)
    for i in range(4):
        step = step1
        if i % 2: # 홀수
            step = step2
        nx, ny = cx + step * dx[i], cy + step * dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            return False
        cx, cy = nx, ny
    
    return True

total = 0
for x in range(2, n):
    for y in range(1, n):
        for step1 in range(1, x):
            for step2 in range(1, x):
                temp = 0
                # 각 꼭지점이 board의 범위를 안넘는지 확인
                if not in_range(step1, step2, x, y):
                    continue
                cx, cy = x, y

                for i in range(4):
                    step = step2 if i % 2 else step1
                    if i % 2: # 홀수
                        step = step2
                    for _ in range(step):
                        nx, ny = cx + dx[i], cy + dy[i]
                        temp += board[nx][ny]
                        cx, cy = nx, ny
                
                if temp > total:
                    total = max(total, temp)
print(total)