from operator import truediv
import math

print("This is a reset i will start python daily from today 11/04/2026")
print("I accept that i have wasted first 100 days of 2026")
print("No matter what happens i will get strong foundation in coding and get place ")
#variable like string int boolean float and following are example demonstrating it

#string a series of characters which also includes numbers
name="nigga"
print("hello "+name)
middle_name="Jamal"
last_name="hell yeah"
print("hello "+name+"\this full name is "+ name+middle_name+last_name)

#int contains numbers
age=25
bill=25000
print("hello",name,"your age is" ,age)
print(f"your total bill is {bill}$")



#flaot also contains numbers but also in decimal forms


run=5.35
gpa=8.63
print(f"i ran over {run}km today")
print("your gpa is",gpa)


#double is also stored decimal values but more decimal points than float
pi=3.1415921213131
print("value of pi is",pi)

#boolen is use for true or false
is_pass=True
is_married=False
print(f"is {name} has passed the exam or not",is_pass)
print("is jamal married or no",is_married)

if is_pass:
    print("Nigga is passed")
else:
    print("Nigga is not passed");


    #typecasting is use to convert one data type into another

print("\n",type(name))
print(type(is_married))
print(type(gpa))
print(type(age))


#explicit conversion
age=float(age)
print(age)
gpa=int(gpa)
print(gpa)

#implicit conversion
x=2
y=2.0

x=x/y
print(x)

name="prithviraj"

age=18

is_student=True

height=1.65

print("Name is"+name+"age is",age,"height is ",height,"is student",is_student)