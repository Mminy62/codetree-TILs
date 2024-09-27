'''
1. 컨베이어벨트를 한줄로 이어서 만들어
2. 시계방향으로 t초만큼 돌린다
'''
n, t = map(int, input().split())
belts = []
for _ in range(2):
    belts += list(map(int, input().split()))

temp = 0
for _ in range(t):
    temp = belts[-1]
    for i in range(n * 2 - 1, 0, -1):
        belts[i] = belts[i - 1]
    belts[0] = temp
        
for i in range(2):
    print(" ".join(map(str, belts[i * n: i * n + n])))