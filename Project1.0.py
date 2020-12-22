def a(x, y, f):
    ans = 0
#   if   x==int and y==int and f==str:
    if   f == "A":
        ans = x + y
    if f == "S":
        ans = x-y
    if f == "M":
        ans = x*y
    if f == "D":
        ans = x/y
#       else:
#            print("enter valid function")
#   else:
#        print("Input proper values")

    print(x," & ",y," are the two numbers and the ", f, " is ", int(ans))

num1=int(input("Enter 1st number"))
num2=int(input("enter 2nd number"))
method=str(input("what function you want to perform,(A/S/M/D)"))
a(num1,num2, method)

