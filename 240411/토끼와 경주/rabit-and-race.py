'''
경주 시작 준비(처음)
N, M, P, pid1 d1 pid2 d2 ,,,
- 처음엔 다 0, 0에 있음
- pid, 한번에 이동하는 거리가 다 다름
dict?


경주 시작
- 가장 우선순위가 높은 토끼를 뽑아서 멀리 보내는걸 K번 반복
- 우선순위: 총 점프수가 적은 토끼, 현재 서있는 행 + 열이 작은 토끼 -> 행번호 작 -> 열번호 -> 고유번호 작은 토끼

- 등률이라면 뒤의까지의 우선순위를 고려해서 정한다. 

- 우선순위 토끼가 정해지면 --
- 4방향을 di만큼 이동시킨 nx, ny를 다 구한다.
이동 중 격자를 벗어나게 되면, 방향을 반대로 바꿔서 한칸 이동 ( 현재 방향에서 반대로 한칸)
- 구해진 4개 위치 중 (행번호 + 열번호가 큰 칸, 행이 큰 칸, 열이 큰 칸 ) 순으로 우선 순위를 두었을때 
    가장 우선순위가 높은 칸을 골라 그 위치로 해당 토끼를 이동
- 이동시킨 칸을 (r, c)면
- i번 토끼를 제외한 나머지 토끼들이!! 전부 r + c만큼의 점수를 얻게 된다 .

=> 차출된 토끼는 점프한거임 -> 점프 횟수 올려주기

K번까지 진행 후 (현재 행 + 열이 큰 번호, 행이 큰 경우, 열이 큰 경우, 고유번호가 큰 경우) 순으로 우선순위를 뽑아 1등에게 S 점수를 더 준다
(단! k번 동안 한번이라도 뽑힌 적이 있어야함이 전제임)


이동거리 변경
- pid 인 토끼의 이동거리를 L배 해준다. 
- 단 계산 도중 토끼의 이동거리가 10억을 넘어가는 일이 없음

최고의 토끼 선정(마지막)
- 각 토끼가 모든 경주를 진행하며 얻은 점수 중 가장 높은 점수 출력

'''

# 점수를 담은 dict, 총 점프수를 담은 dict가 필요 
# 이동 거리를 담은 dict

import heapq
import sys
input = sys.stdin.readline
rabbit_distance = {}
# 경기 상태를 담은 rabbit_pos # 행, 열 
rabbit_pos = {}
rabbit_jump = {}
rabbit_point = {}
rabbit_priority = []
rabbit_priority_keys = {}

def first_rabbit():# 경주 진행을 위해 토끼 선정 
    keys = rabbit_distance.keys()
    # 우선 순위: 점프 횟수가 적, 현재 서있는 행 + 열이 작, 행이 작, 열이 작, 고유번호 작

    if not rabbit_priority:
        for pid in keys:
            heapq.heappush(rabbit_priority, (rabbit_jump[pid], rabbit_pos[pid][0] + rabbit_pos[pid][1], rabbit_pos[pid][0], rabbit_pos[pid][1], pid))
            rabbit_priority_keys[pid] = 0
    else:
        pkeys = rabbit_priority_keys.keys()
        for pid in keys:
            if pid not in rabbit_priority_keys:
                heapq.heappush(rabbit_priority, (rabbit_jump[pid], rabbit_pos[pid][0] + rabbit_pos[pid][1], rabbit_pos[pid][0], rabbit_pos[pid][1], pid))
                rabbit_priority_keys[pid] = 0

    # 점프 수 늘리기
    jid = heapq.heappop(rabbit_priority)[-1]
    rabbit_jump[jid] += 1
    del rabbit_priority_keys[jid]

    return jid

# 뽑힌 토끼에 대한 이동 위치 선정
# 우선 순위: 행 + 열이 큰 것, 행이 큰 것, 열이 큰 것
def first_pos(N, M, pid, K):
    x, y = rabbit_pos[pid]
    pos_q = []
    dx = [0, -1, 1, 0]
    dy = [1, 0, 0, -1]
    dist = rabbit_distance[pid]
    for i in range(4):
        nx = x + dx[i] * dist
        ny = y + dy[i] * dist
        
        # 방향을 넘어간 경우 
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            # 방향을 반대로 바꿔서 이동하는 건지, 아니면 한칸만 이동하는건지??
            if i == 0 or i == 3:
                di = i
                direct = ny // (M - 1)
                move_cnt = ny % (M - 1)
                if direct % 2 == 1: # 홀수인 경우 
                    di = (i + 1) % 3
                
                if di == 0:
                    tempy = move_cnt
                else:
                    tempy = (M - 1) - move_cnt

                tx, ty = nx, tempy
                heapq.heappush(pos_q, (- (tx + ty), -tx, -ty))
            # 
            else:
                di = i
                direct = nx // (N - 1)
                move_cnt = nx % (N - 1)
                if direct % 2 == 1: # 홀수인 경우 
                    di = (i + 1) % 3
                
                if di == 2:
                    tempx = move_cnt
                else:
                    tempx = (N - 1) - move_cnt

                tx, ty = tempx, ny
                heapq.heappush(pos_q, (- (tx + ty), -tx, -ty))

            continue

        # 이동위치가 안넘어간 경우 
        heapq.heappush(pos_q, (- (nx + ny), -nx, -ny))


    # 가장 우선순위가 높은 위치를 골라서 해당 토끼를 이동시킨다. 
    hx, hy = -pos_q[0][1], -pos_q[0][2]
    rabbit_pos[pid] = (hx, hy)

    # 나머지 토끼들은 r + c만큼 점수를 얻는다. 
    keys = rabbit_pos.keys()
    score = (hx + 1) + (hy + 1)
    for key in keys:
        if key != pid:
            rabbit_point[key] += score
    
    return 
    

def first_S(S):
    # S 점수를 부여할 토끼 찾기 
    # 점프 수가 있어야하고, 행 + 열이 큰, 행이 큰거, 열이 큰거, 고유번호 큰거 
    rabbit_S = []
    keys = rabbit_point.keys()
    for key in keys:
        if rabbit_jump[key]:
            r, c = rabbit_pos[key]
            heapq.heappush(rabbit_S, (-(r + c), -r, -c, -key))

    sid = -rabbit_S[0][-1]
    rabbit_point[sid] += S


Q = int(input())
N, M, P = 0, 0, 0
K, S = 0, 0
for _ in range(Q):
    temp = list(map(int, input().split()))
    cmd = temp[0]
    # 준비 
    if cmd == 100:
        N, M, P = temp[1], temp[2], temp[3]
        infos = temp[4:]
        for i in range(P):
            pid, di = infos[i * 2: i * 2 + 2]
            rabbit_distance[pid] = di # 이동 거리 
            rabbit_jump[pid] = 0
            rabbit_pos[pid] = (0, 0)
            rabbit_point[pid] = 0
            
    # 경기 진행 
    if cmd == 200:
        K, S = temp[1], temp[2]
        for _ in range(K):
            jid = first_rabbit()
            first_pos(N, M, jid, K)
            # print("위치:", rabbit_pos)
            # print("점수:", rabbit_point)
        first_S(S)

    # 이동 거리 변경
    if cmd == 300:
        pid, L = temp[1:]
        rabbit_distance[pid] *= L
    
    if cmd == 400:
        keys = rabbit_point.keys()
        max_point = 0
        for pid in keys:
            max_point = max(max_point, rabbit_point[pid])
        
        print(max_point)