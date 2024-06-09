from sortedcontainers import SortedSet

n = int(input())
arr = list(map(int, input().split()))
s = SortedSet([arr[0] - 0])
result = 10 ** 9
for num in arr[1:]:
    s.add(num)
    left = s.bisect_left(num)
    right = s.bisect_right(num)
    if left != len(s):
        result = min(abs(s[left] - num), result)
    
    if right != len(s):
        result = min(abs(s[right] - num), result)
    s.add(num)
    print(result)


# right, left 두번씩 비교