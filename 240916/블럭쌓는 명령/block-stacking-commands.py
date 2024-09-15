'''
N개의 칸이 있다. 
Ai, Bi까지의 각각 블럭을 1씩 쌓으라는 명령이 K번 주어진다. 

'''

N, K = map(int, input().split())

arr = [0] * N
for _ in range(K):
    a, b = map(int, input().split())
    for i in range(a - 1, b):
        arr[i] += 1

arr.sort()
print(arr[N//2])