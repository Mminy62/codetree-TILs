from sortedcontainers import SortedSet

n = int(input())
arr = list(map(int, input().split()))
s = SortedSet([0])
result = 10 ** 9

for num in arr:
    ri = s.bisect_right(num)
    if ri != len(s):
        result = min(result, s[ri] - num)
    result = min(result, abs(s[ri-1] - num))
    s.add(num)
    print(result)


# right, left 두번씩 비교