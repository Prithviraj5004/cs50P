#claculator of week0


a=5
b=67
c=a+b
print(c)

x=float(input("enter value for x:"))
y=float(input("enter value for y:"))
z=x/y

print(f"{z:,.30f}")

#return values
def amin():
    x=float(input("whats the value for x: "))
    print("the square of x is: ",square(x))

def square(x):
    return x*x

amin()
