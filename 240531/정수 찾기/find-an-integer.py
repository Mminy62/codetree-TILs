n = int(input())
a = set(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))

for item in b:
    if item in a:
        print(1)
    else:
        print(0)