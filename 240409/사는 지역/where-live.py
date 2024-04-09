class Person:
    def __init__(self, name, address, location):
        self.name = name
        self.address = address
        self.location = location
    
    def output(self):
        print("name", self.name)
        print("addr", self.address)
        print("city", self.location)
        return


n = int(input())
name, add, loc = input().split()
ans = Person(name, add, loc)

for _ in range(1, n):
    name, add, loc = input().split()
    if ans.name < name:
        ans = Person(name, add, loc)

ans.output()