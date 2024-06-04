'''
TreeSet: 균형잡힌 이진트리, sorted 이진트리
삽입, 삭제 탐색 등 모든 함수의 시간 복잡도 O(logN)
기본적으로 오름차순으로 정렬됨

다른 set처럼 s.add, s.remove(E), E in s 는 똑같고,
s.bisect_left(E) 이진탐색 함수가 가능함.
E보다 같거나 큰 최초의 데이터가 들어있는 index를 반환한다. 
없으면 마지막 인덱스를 반환한다
// 이진 탐색으로 해당 E가 들어갈 자리를 준다고 생각하면 편함

s.bisect_right(E)
E보다 큰 최초의 데이터 index를 반환

'''

from sortedcontainers import SortedSet

s = SortedSet()
n = int(input())
for _ in range(n):
    cmds = list(input().split())
    num = int(cmds[1]) if len(cmds) == 2 else 0
    cmd = cmds[0]

    if cmd == "add":
        s.add(num)
    elif cmd == "remove":
        s.remove(num)
    elif cmd == "find":
        if num in s:
            print("true")
        else:
            print("false")
    elif cmd == "lower_bound":
        idx = s.bisect_left(num)
        if idx == len(s):
            print("None")
        else:
            print(s[idx])

    elif cmd == "upper_bound":
        idx = s.bisect_right(num)
        if idx == len(s):
            print("None")
        else:
            print(s[idx])
    elif cmd == "largest":
        if not s:
            print("None")
        else:
            print(s[-1])
    else:
        if not s:
            print("None")
        else:
            print(s[0])