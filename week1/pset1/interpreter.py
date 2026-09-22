#1 ask user for input
#2 simple math calculation
#3 display output in float
import math

user=input("Enter expression:")
expression=user.strip()
x,y,z=expression.split()
x=int(x)
z=int(z)

if y=="+":
    result=int(x+z)
    print(float(result))
elif y=="-":
    result=int(x-z)
    print(float(result))
elif y=="*":
    result=int(x*z)
    print(float(result))
else:
    if z=="0":
        print("cant divide by zero")
    else:

        print(float(x/z))

