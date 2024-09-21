N, M = map(int, input().split())

board = []
result = 0
for _ in range(N):
    board.append(list(map(int, input().split())))

def search(flag):
    global result

    for i in range(N):
        cnt = 1
        pre = board[i][0] if flag else board[0][i]
        for j in range(1, N):
            (r, c) = (i, j) if flag else (j, i)
            if board[r][c] == pre:
                cnt += 1
            if board[r][c] != pre:
                if cnt >= M:
                    result += 1
                    break
                cnt = 1
                pre = board[r][c]
            if j == N - 1:
                if cnt >= M:
                    result += 1

result = 0
if N == 1 and M == 1:
    result += N * 2

else: # N > 1
    search(1)
    search(0)

print(result)