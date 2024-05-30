from sortedcontainers import SortedDict

n = int(input())
sd = SortedDict()

for _ in range(n):
    arr = list(input().split())
    if arr[0] == "add":
        sd[int(arr[1])] = int(arr[2])

    elif arr[0] == "remove":
        sd.pop(int(arr[1]))

    elif arr[0] == "find":
        if int(arr[1]) in sd:
            print(sd[int(arr[1])])
        else:
            print("None")
    else:
        tmp = sd.values()
        if tmp:
            print(' '.join(map(str, tmp)))
        else:
            print("None")