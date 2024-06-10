'''
m 개의 비어있는 의자, 
1-m개 번호
n개의 원하는 번호 숫자
i번째 사람은 1~ ai 의자에만 앉고 싶다는 것, 
1번 사람부터 순서대로 
최초로 앉지 못하는 사람이 생기면 종료

앉게되는 사람의 수를 최대로 만들어라
ai가 최대한 안겹치게 최대 숫자에 앉으면 되지 않나?


앉는 의자를 set에 넣어놓고, 사람의 순서대로 ai번-1번까지 희망하는 숫자 후보가 있으면 삭제하고, 없으면 종료 -> 일반 set을 이용해도 됨
SortedSet을 이용하려면?
해당 의자를 넣으면서, 이미 있는 값이면 안넣고, 이전값으로 계속 -1 시키기

'''
from sortedcontainers import SortedSet

n, m = map(int, input().split())
s = SortedSet([i for i in range(1, m + 1)])
ans = 0

arr = list(map(int, input().split()))
for num in arr:
    flag = False
    for i in range(num, 0, -1):
        if i not in s:
            if i == 1:
                flag = True
            else:
                continue
        else:
            s.remove(i)
            ans += 1
            break
    if flag:
        break
    

print(ans)