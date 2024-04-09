'''

'''
N, T = map(int, input().split())

r, c, d = input().split()
r, c = int(r), int(c)

r, c = r - 1, c - 1
dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]

di = 0

if d == 'R':
    di = 0
elif d == "U":
    di = 1
elif d == "D":
    di = 2
else:
    di = 3

time = 0
while time != T:
    time += 1
    nx = r + dx[di]
    ny = c + dy[di]
    
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        di = (3 - di)
        continue
    # 아닌 경우 
    r, c = nx, ny

print(r + 1, c + 1)