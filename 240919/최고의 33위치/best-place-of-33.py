'''
완전탐색 구현 방법은
1. for문
2. 재귀함수 기반 backtracking(brute force)


'''

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

result = 0
for i in range(N - 2):
    for j in range(N - 2):
        temp = 0
        for dx in range(3):
            for dy in range(3):
                x = i + dx
                y = j + dy
                if board[x][y]:
                    temp += 1
        result = max(result, temp)

print(result)