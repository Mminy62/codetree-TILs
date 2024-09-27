'''
바람을 처음에 맞은 행이 움직이고, 
그 행의 위, 아래 행 중에서, 같은 열에 같은 숫자가 있다면 전파되어 반대방향으로 1칸씩 움직인다. 
    - 만일, 같은 숫자가 열에 하나도 존재하지 않거나, 끝(0, N행 윗부분)에 다다랐다면 전파를 종료한다.

- 방향을 밀때 (방향 정보 필요, -1로 토글하기)

N, M 

'''
from collections import deque

N, M, Q = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


# 방향대로 한줄씩 옮겨주는 함수 필요
def shift(row, direct):
    if direct == "L": # 시계 방향
        temp = arr[row][-1]
        for i in range(M - 1, 0, -1):
            arr[row][i] = arr[row][i - 1]
        arr[row][0] = temp
    else:
        temp = arr[row][0]
        for i in range(M - 1):
            arr[row][i] = arr[row][i + 1]
        arr[row][M - 1] = temp

# 중복이 있는지 체크하는 함수
def check_correct(r1, r2):
    for item in zip(arr[r1], arr[r2]):
        if item[0] == item[1]:
            return True
    return False
    
def in_range(nx):
    if nx < 0 or nx >= N:
        return False
    return True

def reverse_direct(direct):
    if direct == "L":
        return "R"
    else:
        return "L"

def up_down(idx):
    directs = {0: [-1], 1: [1], 2: [-1, 1]}
    return directs[idx]

for _ in range(Q):
    row, direct = input().split()
    row = int(row) - 1

    q = deque([(row, direct, 2)])
    while q:
        row, direct, spreads = q.popleft()
        shift(row, direct)
        
        for di in up_down(spreads):
            direct_row = row + di

            if in_range(direct_row) and check_correct(row, direct_row):
                if direct_row == -1:
                    spread = 0
                else:
                    spread = 1
                q.append((direct_row, reverse_direct(direct), spread))

for i in range(N):
    print(" ".join(map(str, arr[i])))