from collections import deque
arr = deque([])
for _ in range(5):
    arr.append(deque(list(input())))

result = ''
while arr:
    line = arr.popleft()
    if line:
        result += line.popleft()
    if line:
        arr.append(line)

print(result)