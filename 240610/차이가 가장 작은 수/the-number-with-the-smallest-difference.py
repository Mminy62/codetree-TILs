import sys
from sortedcontainers import SortedSet

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
arr = [
    int(input())
    for _ in range(n)
]

# 입력으로 주어진 숫자를 전부 treeset에 넣어줍니다.
s = SortedSet(arr)

# 답을 저장합니다.
ans = INT_MAX

# 각 숫자 x 대해
# x보다 m 이상 더 크면서 가장 작은 값과
# x보다 m 이상 더 작으면서 가장 큰 값을 구해
# 차이가 가장 작은 경우를 갱신합니다.
for x in arr:
    # x보다 m 이상 더 크면서 가장 작은 값은
    # r - x >= m를 만족하는 최소 r이므로
    # r >= m + x을 만족하는 최소 r을 구하면 됩니다.
    min_idx = s.bisect_left(m + x)
    if min_idx != len(s):
        ans = min(ans, s[min_idx] - x)


# 불가능하다면 -1을 넣어줍니다.
if ans == INT_MAX:
    ans = -1

print(ans)