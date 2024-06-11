'''
rc x 
x가 1인경우

문제번호가 큰것 
문제번호가 작은 것으루


rc는 문제 리스트에 문제가 1개 이상일때만 주어진다. 
x는 반드시 1 -1로 주어진ㄷ. 

ad 난이도 L, 문제 번호 P
'''
# 난이도별 리스트를 만들어서 문제번호를 담고 있는다. 난이도별 문제 이중 SortedSet?..
from sortedcontainers import SortedSet
n = int(input())

s = SortedSet()
for _ in range(n):
    P, L = map(int, input().split())
    s.add((L, P))

m = int(input())
for _ in range(m):
    cmds = input().split()
    if cmds[0] == "ad":
        P, L = int(cmds[1]), int(cmds[2])
        s.add((L, P))
    elif cmds[0] == "sv":
        P, L = int(cmds[1]), int(cmds[2])
        s.remove((L, P))
    else:
        if int(cmds[1]) == 1:
            print(s[-1][1])
        else:
            print(s[0][1])