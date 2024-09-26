'''
양수 직사각형 중 가장 큰 크기
직사각형 안에 숫자들이 전부 양수인 경우
최대 크기 즉, width, height가 최대인 걸 구해라. 

'''

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def check_positive(sx, sy, ex, ey):
    for x in range(sx, ex):
        for y in range(sy, ey):
            if grid[x][y] <= 0:
                return False
    return True

result = 0
for height in range(1, N + 1):
    for width in range(1, M + 1):
        for i in range(N):
            for j in range(M):
                nx, ny = i + height, j + width
                if nx < 0 or nx > N or ny < 0 or ny > M:
                    continue
                if check_positive(i, j, nx, ny):
                    result = max(result, height * width)


print(result)