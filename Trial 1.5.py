thisDict = {
    "brand":"Ford",
    "electirc": False,
    "Year": 1980,
    "Colors":["red","white","blue"]
}
print(type(thisDict))
print(thisDict)
print(thisDict["brand"])
print(thisDict.get("brand"))
print(thisDict.keys())
thisDict["Year"]=2020
print(thisDict)
print(thisDict.values())
print(thisDict)
print(thisDict.items())
if "brand" in thisDict:
    print("\'brand\' is a key on \'thisDict\'")
thisDict["Year"]=2018
print(thisDict)
thisDict.update({"Year":2019,"model":"xysa"})
print(thisDict)
thisDict.pop("brand")
print(thisDict)
thisDict.update({"brand":"ford","Colors":["red","green"]})
print(thisDict)
del thisDict["brand"]
print(thisDict)
for x in thisDict:
    print(x)
    print("Key is "+x+" and the value for "+x+" is ", end="")
    print(thisDict[x])
for x in thisDict.values():
    print(thisDict.keys(), end="")
    print(x)
for x, y in thisDict.items():
    print(x, y)
a,b = 20,10
print("a is ",end="") if a > b else print("a & b are ", end="") if a == b else print("b is ", end="")
print("greater")
import random
i = random.randint(0, 100)
while i !=5:
    i = random.randint(0, 81)
    if i > 80:
        print("value of i is ", end="")
        print(i, end="")
        print(" hence closing the loop ")
        break
    if i < 20:
        print(" value of i ", end="")
        print(i, end="")
        print(" LESS THAN 20")
        continue
    print(i)
print(i)
