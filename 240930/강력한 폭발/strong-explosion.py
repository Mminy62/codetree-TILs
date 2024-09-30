'''
n * n 크기의 격자판
1 - 폭탄을 놓을 수 있고
최대화 하려고한다.

움.. 1, 2, 3을 다 도렴
visited를 만들어서, 1, 2, 3을 다 해보면 되지 않나?..

400, 
안겹치는 가장 많은 경우의수,,

0을 가장 많이 칠하는 경우의 수를 선택하자 1, 2, 3중

1의 개수만큼 1, 2, 3 을 다 선택해보는 경우의 수

하고 완탐

'''

n = int(input())
board = []
cnt = 0 
pos = []
result = 0
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j]:
            pos.append((i, j))
            cnt += 1
    board.append(line)

arr = []

# cnt 개수만큼 백트래킹으로 1, 2, 3 

distance = {1: [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)], 2: [(-1, 0), (0, 0), (1, 0), (0, -1), (0, 1)], 3: [(-1, -1), (0, 0), (-1, 1), (1, -1), (1, 1)]}

def search():
    global result
    visited = [[0] * n for _ in range(n)]
    
    for (x, y), num in zip(pos, arr):
        for dx, dy in distance[num]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            visited[nx][ny] = 1
    
    temp = 0
    for i in range(n):
        temp += visited[i].count(1)
    
    result = max(result, temp)
    return

def dfs():
    if len(arr) == cnt:
        search()
        return

    for num in range(1, 4):
        arr.append(num)
        dfs()
        arr.pop()

dfs()

print(result)