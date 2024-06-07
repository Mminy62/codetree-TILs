# 삽입되는 값에 중복되는 숫자는 주어지지 않습니다. 라는 말때문에 중복되는 숫자가 없다는 것에서 -> Set 사용
# 최대값, 최소값을 매 명령어마다 알기 위해서 시간절약을 위해 SortedSet을 사용했다. 

from sortedcontainers import SortedSet

T = int(input())

for _ in range(T):
    k = int(input())
    s = SortedSet()

    for _ in range(k):
        cmd, num = input().split()
        num = int(num)

        if cmd == "I":
            s.add(num)
        elif cmd == "D":
            if not s:
                continue

            if num == 1:
                s.remove(s[-1])
            else:
                s.remove(s[0])
    
    if not s:
        print("EMPTY")
    else:
        print(s[-1], s[0])