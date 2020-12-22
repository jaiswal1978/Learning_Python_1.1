f = open("FileReading.txt","a")
#print(f.read())
#print(f.readline())
#print(f.readline())
#for x in f:
#    print(x)
#f.close()
try:
    print(f.readline())
    print("code executed successfully")
except:
    print("some error occur")
finally:
    print("the code is completed")
f.write("now this is more content")
f.close()
f = open("FileReading.txt", "r")
print(f.readline())
f.close()
import os
files = os.listdir("D:\Python\Trial Project 1.1")
for i in files:
    print(i)
os.remove("FileReading.txt")
files = os.listdir("D:\Python\Trial Project 1.1")
for i in files:
    print(i)
f = open("FileReading.txt","x")
f.write("this is sample text")
f.close()
f = open("FileReading.txt","r")
print(f.readline())
f.close()
f = open("FileReading.txt", "a")
f.write("this is line 2")
f.close()
f = open("FileReading.txt","r")
print(f.readline())
if os.path.exists("thisissample.txt"):
    print("file named \'thisissample.txt\' exist")
    files = os.listdir("D:\Python\Trial Project 1.1")
    for i in files:
        print(i)
    os.remove("thisissample.txt")
    print("file name \'thisissample.txt\' have been deleted")
    files = os.listdir("D:\Python\Trial Project 1.1")
    for i in files:
        print(i)
else:
    print("file name \'thisissample.txt\' is not there. Python will now create a new file with this name")
    f = open("thisissample.txt","x")
    f.write("this is a sample statement 1")
    f.close()
    f = open("thisissample.txt", "r")
    print(f.readline())
    f.close()
    files = os.listdir("D:\Python\Trial Project 1.1")
    for i in files:
        print(i)





