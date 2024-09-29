# n자리 아름다운 수의 개수를ㅊㄹ력한다. 
from collections import deque
n = int(input())
result = 0

def check(arr):
    num = arr[0]
    for i in range(1, len(arr)):
        if num != arr[i]:
            return False
    return True

def is_beautiful(numbers):
    cur = 0
    length = len(numbers)
    while cur < length:
        step = int(numbers[cur])
        if cur + step > length:
            return False
        if not check(numbers[cur: cur + step]):
            return False
        cur = cur + step
    return True

def dfs(arr):
    global result
    if len(arr) == n:
        if is_beautiful(arr):
            result += 1
        return 
    
    for num in ['1', '2', '3', '4']:
        arr.append(num)
        dfs(arr)
        arr.pop()

dfs([])

print(result)