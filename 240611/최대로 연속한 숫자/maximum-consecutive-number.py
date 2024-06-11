'''
n까지 숫자들
연속하여 나타나는 숫자들로만 이루어진 최장길이 LIS 구하기

'''
from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))

s = [SortedSet([i for i in range(n + 1)])]

# m개의 split Set을 만들면 안되나?

for num in arr:
    for sen in s:
        if num in sen:
            idx = sen.bisect_left(num)
            s.remove(sen)
            s.append(SortedSet(sen[:idx]))
            s.append(SortedSet(sen[idx + 1:]))
            break

    res = 0
    for sen in s:
        res = max(res, len(sen))
    
    print(res)