#format strings
quantity=5
article = "apples"
rate = 50.0
order = "We supply premium quality {} at the rate of {} for {} {}"
print(order.format(article,rate,quantity,article))
#format strings
quantity=5
article = "apples"
rate = 50.0
order = "We supply premium quality {0} at the rate of {1} for {2} {0}"
print(order.format(article,rate,quantity))
#escape characters
print("it\'s ok")
print("this will insert one \\ backslash")
#print("this is first line \nthis is second line")
print("hello\rworld")
print("hello\tworld")
print("hello\bworld with back space")
print("hello\fworld with form field")
print("this is octal vale \120")
#string methods
a = "this is a simple statement to try out string methods in PYTHON"
print(a.capitalize()+" - capitalize")
print(a.casefold()+" - casefold")
print(a.swapcase()+" - swapcase")
print(a.center(100)+" - center")
print(a.count("i"))
x=20.3
print(isinstance(x,int))
print(isinstance(x,float))
print(isinstance(x,str))
print("large") if 2>10 else print("small")
list = ["apples","banana","cherry","grapes"]
print(list[-1])
print(len(list))
print(list[-3:-1])
if "apples" in list:
    print("yes apples in list")
list[0]="xyz"
print(list)
list[0:4]=["x","y","z"]
print(list)
list.insert(0,"a")
print(list)
list.append("fdf")
print(list)
list1=[0,9,89.6,True,78,"thy"]
print(list1)
list.extend(list1)
print(list)
list.remove(0)
print(list)
list.pop(-2)
print(list)
del list[-3]
print(list)
print(list1)
for x in list:
    print(x)
for i in range(len(list)):
    #print(list[i])
    print(i)
j=0
while j < len(list):
    print(list[j])
    j=j+1
list=["apples","banana","cherry","mango"]
print(list)
newlist=[]
print(newlist)
for x in list:
    if  "a" in x:
        newlist.append(x)
print(newlist)
Newlist = [x for x in list if "a" in x]
print(Newlist)
list=[x for x in range(10)]
print(list)
list=[x for x in range(100) if (x % 2)!=0]
print(list)
list=[x for x in range(100) if (x % 2)==0 and x >10 and x <50]
print(list)
print(list1)
print(ord("a"))
list.clear()
#generate a list containing randomly generated string
import random
#for x in range(10):
#    list.append(chr(random.randrange(97,122,1))+chr(random.randrange(97,122,1))+chr(random.randrange(97,122,1))+chr(random.randrange(97,122,1)))
#print(list)

for x in range(10):
    z_var = ""
    for y in range(5):
        z_var += chr(random.randrange(97,122,1))
    list.append(z_var)

print(list)
list1 = [x.upper() for x in list]
print(list1)
newlist = [x.capitalize() for x in list]
print(newlist)
list2 = ["hello" for x in list]
print(list2)
list2 = [x if "u" not in x else "null" for x in list]
print(list2)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)