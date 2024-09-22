# 블럭을 놓고, 그 안에 최대의 숫자 탐색
# 각 블럭을 90도씩 회전한 모형에, 뒤집은 케이스까지 곱해서 좌표 알아내기
N, M = map(int, input().split())

first = [[(0, 0), (1, 0), (1, 1)], [(0, 0), (0, 1), (1, 0)], [(0, 0), (0, 1), (1, 1)], [(1, 0), (1, 1), (0, 1)]]
second = [[(0, 0), (0, 1), (0, 2)], [(0, 0), (1, 0), (2, 0)]]
cases = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

result = 0

def fold(arrs):
    global cases
    result = []
    for arr in arrs:
        for cx, cy in cases:
            temp = []
            for x, y in arr:
                temp.append((x * cx, y * cy))
            result.append(temp)
    return result

def bfs(i, j, arrs):
    global result
    for arr in arrs:
        temp_result = 0
        for dx, dy in arr:
            nx, ny = i + dx, j + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                temp_result = 0
                break
            temp_result += board[nx][ny]
        
        result = max(result, temp_result)

first_fold = fold(first)
second_fold = fold(second)
for i in range(N):
    for j in range(M):
        bfs(i, j, first)
        bfs(i, j, second)
        bfs(i, j, first_fold)
        bfs(i, j, second_fold)

print(result)