'''
K가 0 = 1곳
손해보지 않으면서 가장 많은 금의 개수를 출력
채굴비용이 있기 때문에 손해볼 수 있음

색칠해진 구간 중 최대의 금액을 갖고있는 경우에서 안에 있는 금의 개수 구하기

=> 최대 금액을 갖고 있는 구역 알아내기

n <= 20, m <= 10

특정 점을 중심으로 완전탐색?
k <= 20
400 * 10 * 약 몇백~K*K+(K+1)*(K+1
'''

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

result = 0
result_cnt = 0

for x in range(n):
    for y in range(n):
        for k in range(n):
            cost = - ( k * k + (k + 1) * (k + 1) )
            cnt = 0
            for t in range(k + 1): #윗부분
                for ny in range(y - (k - t), y + (k - t) + 1):
                    nx = x - t
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if board[nx][ny] == 1:
                        cost += m
                        cnt += 1
            
            for t in range(1, k + 1): #아랫부분
                for ny in range(y - (k - t), y + (k - t) + 1):
                    nx = x + t
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if board[nx][ny] == 1:
                        cost += m
                        cnt += 1
            if cost >= 0:
                result_cnt = max(result_cnt, cnt)

print(result_cnt)