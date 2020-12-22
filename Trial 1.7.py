x= lambda a,b: a*b
print(x(2,3))
class MyClass:
    x = 5
print(MyClass)
p1=MyClass()
print(p1.x)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print(self.name,self.age)
p1 = Person("Sam",36)
p1.myfunc()
class student(Person):
    pass
x= student("xyz","abc")
x.myfunc()

