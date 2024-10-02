from collections import deque
arr = []
for _ in range(5):
    arr.append(deque(list(input())))

result = ''
while arr:
    for i in range(len(arr)):
        if arr[i]:
            result += arr[i].popleft()
        else:
            arr.pop(i)
            break

print(result)