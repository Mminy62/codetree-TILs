'''
배수의 관계이면 가장 큰 걸로 나눠주기 시작하는 것이 좋다

'''
import sys
sys.setrecursionlimit(10**5)

n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.reverse()

# if result < 0 : break
def dfs(num, cnt):
    if num < 0:
        return -1

    if num == 0:
        return cnt

    for i in range(n):
        if num - arr[i] >= 0:
            return dfs(num - arr[i], cnt + 1)

answer = 10 ** 9
for i in range(n):
    temp = dfs(k - arr[i], 1)
    if temp != -1:
        answer = min(answer, temp)

print(answer)