'''
중간의 값에 접근하면서, 정렬을 유지하는 형태 -> SortedSet(TreeSet)

'''
from sortedcontainers import SortedSet

n, m = map(int, input().split())
nums = list(map(int, input().split()))
s = SortedSet([i for i in range(1, m + 1)])

for num in nums:
    s.remove(num)
    print(s[-1])