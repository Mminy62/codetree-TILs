'''
n명의 
같은 사람이 동시에 여러 그룹에 속할 수 있다
그룹 내에 모든 멤버가 정확히 일치하는 두 그룹은 없다
그룹 인원수가 k인 그룹에서 k - 1명의 사람들이 초대장을 받았다면, 나머지 한 사람도 무조건 초대장을 받아야한다.

'''

invited = set([1])
n, g = map(int, input().split())
arr = []
for _ in range(g):
    tmp = list(map(int, input().split()))
    tmp = [tmp[0]] + sorted(tmp[1:])
    arr.append(tmp)

arr.sort()

for people in arr:
    num = people[0]
    print(invited, people[1:])
    people = set(people[1:]) - invited
    if len(people) == 1:
        invited = invited | people


print(len(invited))