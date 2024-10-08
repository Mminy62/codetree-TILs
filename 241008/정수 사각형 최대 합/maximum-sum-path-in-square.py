n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 가로
for j in range(1, n):
    board[0][j] += board[0][j - 1]
# 세로
for i in range(1, n):
    board[i][0] += board[i - 1][0]

for i in range(1, n):
    for j in range(1, n):
        board[i][j] += max(board[i - 1][j], board[i][j - 1])

print(board[n - 1][n - 1])