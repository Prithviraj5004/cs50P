# loops
#1 while loop



while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

#lists are the data represented using[] brackets

names=["harish","prithviraj","prasad"]
for i in range(len(names)):
    print(i+1,names[i])
students=[
    {"name":"prithviraj","address":"pune","gpa":"8.63"},
    {"name": "aditya", "address": "nashik", "gpa": "7.63"},
    {"name": "sandesh", "address": "beed", "gpa": "9.63"},
    {"name": "vedant", "address": "mumbai", "gpa": "8.95"}

]
for student in students:
    print(student["name"],student["address"],student["gpa"],sep=",")
