'''
총 N번 움직이기 
N번 걸쳐 움직이려는방향, 
'''
time = 0
direct = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}

cmd = int(input())
start = (0, 0)
temp = [0, 0]
ans = -1
x, y = temp
for _ in range(cmd):
    direct_key, value = input().split()
    value = int(value)
    dx, dy = direct[direct_key]

    for k in range(value):
        nx, ny = x + dx, y + dy
        time += 1
        if (nx, ny) == start:
            ans = time
            break
        x, y = nx, ny
    if ans != -1:
        break

print(ans)