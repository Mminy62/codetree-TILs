n = int(input())
s = set()
for _ in range(n):
    cmd, item = input().split()
    if cmd == "add":
        s.add(item)
    elif cmd == "remove":
        s.remove(item)
    else:
        if item in s:
            print("true")
        else:
            print("false")