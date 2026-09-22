# this i week 0 of cs50 python course
# i will learn all this by my self
#https://docs.python.org/3/library/functions.html
#https://cs50.harvard.edu/python/notes/0
#notes and source code


# ask user for input
#name=input("Enter Your name: ").strip().title()
#first,middle,last=name.split(' ')
#print(f"hello,{first}")

#defining functions
def main():
    name=input("Enter your name:")
    hello(name)



def hello(to="world"):
    print("hello",to)

main()


