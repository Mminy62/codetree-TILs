class Person:
    def __init__(self, value, level):
        self.value = value
        self.level = level
    
    def output(self):
        print("user", self.value, "lv", self.level)



idvalue, level = input().split()


Person("codetree", "10").output()

Person(idvalue, level).output()