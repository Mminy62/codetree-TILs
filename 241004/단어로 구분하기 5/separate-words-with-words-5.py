import sys
input = sys.stdin.readline

arr = list(input().split())
for i in range(len(arr)):
    if i % 2:
        print(arr[i])