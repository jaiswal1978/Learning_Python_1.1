#generate a list having random integers where each integer is between 1000 to 9999 starting with 1000 and ending with 9999
import random
list10 = [1000]
list4 = []
print(list10)
for x in range(10):
    list10.append(random.randint(1000, 9999))
    list4.append(random.randint(100,999))
list10.append(9999)
#Sorting the list
list10.sort()
print(list10)
list10.sort(reverse=True)
print(list10)
# sort the list generated above based on how close the number is to 5555
def myFunc(n):
    return abs(n-5555)
list10.sort(key=myFunc)
print(list10)
list1=list10
list2 = list10.copy()
list10.append(99)
print(list10)
print(list1)
print(list2)
print(list4)
list5=[]
print(list5)
for x in list10:
    list5.append(x)
for x in list1:
    list5.append(x)
print(list5)
tuple1 = ("class")
tuple2 = ("class",)
print(type(tuple1))
print(type(tuple2))
tuple1 = tuple(("apple","cls",1,2,True))
print(tuple1)
x=list(tuple1)
print(type(x))
print(x)
x[0] = "kiwi"
tuple1=tuple(x)
print(tuple1)
set_example = {"ahkuhku","apples","banana","kiwi","kiwi"}
print(set_example)
set_example1 = {1,2,34,5,6,True,False}
set_example.add("last")
print(set_example)
set_example.update(tuple1)
print(tuple1)
print(set_example)
del set_example
set_example=set_example1=set_example2={}
print(set_example)
print(set_example1)
print(set_example2)
set_example = {"apples","banaba","cherry","kiwi"}
set_example1 = {"kiwi","apples","dvgsf","hekfhkudha"}
print(set_example)
print(set_example1)
set_example1.intersection_update(set_example)
set_example2=set_example.intersection(set_example1)
set_example3 = set_example.symmetric_difference(set_example1)
set_example4 = set_example1.symmetric_difference(set_example)
print(set_example)
print(set_example1)
print(set_example2)
print(set_example3)
print(set_example4)

