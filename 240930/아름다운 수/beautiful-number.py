# n자리 아름다운 수의 개수를ㅊㄹ력한다. 
from collections import deque
n = int(input())
result = 0
arr = []

def is_beautiful():
    cur = 0

    while cur < n:
        step = arr[cur]

        if cur + arr[cur] - 1 >= n:
            return False

        for j in range(cur, cur + step):
            if arr[j] != arr[cur]:
                return False
        cur = cur + step

    return True

def dfs():
    global result, arr
    if len(arr) == n:
        if is_beautiful():
            result += 1
        return 
    
    for num in range(1, 5):
        arr.append(num)
        dfs()
        arr.pop()

dfs()

print(result)