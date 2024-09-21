N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# 행끼리 비교
result = 0
for i in range(N):
    cnt = 0
    pre = 0
    for j in range(N):
        if cnt == 0:
            cnt += 1
            pre = board[i][j]
        else:
            if board[i][j] == pre:
                cnt += 1
            if board[i][j] != pre or j == N - 1:
                if cnt >= M:
                    result += 1
                cnt = 1
                pre = board[i][j]

for i in range(N):
    cnt = 0
    pre = 0
    for j in range(N):
        if cnt == 0:
            cnt += 1
            pre = board[j][i]
        else:
            if board[j][i] == pre:
                cnt += 1
            if board[j][i] != pre or j == N - 1:
                if cnt >= M:
                    result += 1
                cnt = 1
                pre = board[j][i]

print(result)