from classobjinher import student
import

class myclass:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = myclass('pavan',58)
print(p1.name)

class person(student):
    pass

p2 = person()
print(p2.name)