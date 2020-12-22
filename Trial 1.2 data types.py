x=5
y="shihbjbn"
print("type of x = ", end="")
print(type(x))
print("type of y = ")
print(type(y))
#data types
#x= {"name":"john","age":32,"float":10.2,"complex":7j}
x=3e-4
y=complex(x)
print(type(x), end="")
print(x)
print(type(y), end="")
print(y)
#random number
import random
for a in range(6):
    print(random.randrange(1,10))
#strings
a="""wshfhejdhgkjhkgbndkgjhkjdsgkj
dgsjkgdls;gj
sdgjisjgij
sdgsjg"""
print(a)
a="djkgkjhds"\
  "sdgijsdigj"\
  "dsgjisjgi" \
  "agjisdaj" \
  "sdahguasdhg"
print(a)
a=" hello world "
print(a[8])
print(len(a))
print("for loop starts")
for x in "the banana":
    print(x)
print("a" in x)
#in function
if "he" in a:
    print("\"he\" is present in "+a)
else:
    print("\"he\" not in "+a)
if "he" not in a:
    print("\"he\" is not in " + a)
else:
    print("\"he\" is in " + a)
print(a[2:7])
print(a[-4:])
print(a.upper())
print(a.lower())
print(a.strip()+"/"+a)
print(a.replace("h","z"))
print(a.split(" "))
print(a.split("l"))