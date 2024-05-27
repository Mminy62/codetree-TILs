n = int(input())

menu = {}
for _ in range(n):
    arr = list(input().split())
    cmd = arr[0]
    arr = arr[1:]
    if cmd == "add":
        key, value = arr
        menu[key] = value
    if cmd == "find":
        if arr[0] in menu:
            print(menu[arr[0]])
        else:
            print("None")

    if cmd == "remove":
        menu.pop(arr[0])