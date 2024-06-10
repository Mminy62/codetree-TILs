'''
Sort와 시간복잡도는 O(NlogN)으로 같지만, 중복을 제외한다는 것에서, 이중 작업을 방지하기위해 SortedSet을 사용하는 것이다.
'''
from sortedcontainers import SortedSet
n, k = map(int, input().split())
arr = list(map(int, input().split()))

s = SortedSet(arr)
result = s[-k:]
for i in range(len(result) - 1, - 1, - 1):
    print(result[i], end=" ")