'''
0을 기준으로 0이 속해있었던 그룹에 제거할게 있는지 확인하는 것

'''

from collections import deque

n, g = map(int, input().split())
invited = [False] * n

groups = [set() for _ in range(g)]

people_groups = [[] for _ in range(n)] # 각 사람이 어느 그룹에 속해있는지 그룹 숫자를 추가
q = deque()
ans = 0

for i in range(g):
    nums = list(map(int, input().split()))[1:]
    for num in nums:
        num -= 1
        groups[i].add(num)
        people_groups[num].append(i) # n명이 각각 몇번째 그룹에 속해있는지 체크..

q.append(0)
invited[0] = True
while q:
    person = q.popleft()
    
    group_nums = people_groups[person]
    for g_num in group_nums:
        groups[g_num].remove(person)

        if len(groups[g_num]) == 1:
            num = list(groups[g_num])[0]

            if not invited[num]:
                invited[num] = True
                q.append(num)

print(len(list(filter(lambda x: x == True, invited))))