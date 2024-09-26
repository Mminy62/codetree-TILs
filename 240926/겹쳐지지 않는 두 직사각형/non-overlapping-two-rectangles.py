'''
N * M 크기의 이차원 영역의 정수값이 하나씩
- 겹치지 않는 두 직사각형, 최대합
- 이제까지 최대합은 완전탐색으로만 해봤는데,,, -가 있다보니 전체를 더할 순 없음

음.. 겹치지 않는 두 직사각혀,,
크기도 정해지지 않으니까
최대 N, M 
가장 최대의 합 1, 그 다음 차선책 1개로 해서 만들어야할듯

x <= N, y <= M


'''
import heapq
import sys
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
q = []

def is_not_overlapping(rect1, rect2):
    r1, c1, r2, c2 = rect1
    x1, y1, x2, y2 = rect2
    # if rect1[3] < rect2[1] or rect2[3] < rect1[1]: #열
    #     return True
    # if rect1[2] < rect2[0] or rect2[0] < rect1[2]: #행
    #     return True

    if x2 <= r1 or r2 <= x1:
        return True
    if c2 <= y1 or y2 <= c1:
        return True
    
    return False

for height in range(1, N + 1):
    for width in range(1, M + 1):
        if height == N + 1 and width == M + 1: #전체 사각형이면 안됨
            continue
        for x in range(N):
            for y in range(M):
                last_height, last_width = x + height, y + width
                if last_height < 0 or last_height > N or last_width < 0 or last_width > M:
                    continue
                temp = 0
                for nx in range(x, last_height):
                    for ny in range(y, last_width):
                        temp += board[nx][ny]
                heapq.heappush(q, (-temp, x, y, height, width))

result = -sys.maxsize
length = len(q)                
for i in range(length):
    rsize1 = -q[i][0]
    rx1, ry1, rh1, rw1 = q[i][1:]
    rect1 = [rx1, ry1, rx1 + rh1, ry1 + rw1]
    

    for j in range(length):
        if i == j:
            continue
        rsize2 = -q[j][0]
        rx2, ry2, rh2, rw2 = q[j][1:]
        rect2 = [rx2, ry2, rx2 + rh2, ry2 + rw2]
        if is_not_overlapping(rect1, rect2):
            result = max(result, (rsize1 + rsize2))


print(result)