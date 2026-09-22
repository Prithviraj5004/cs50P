#1 ask user for input of greetings
#2 if greeting is hello output is $0
#3 if it start with h like hey then output is $20
#4 else output is $100

greetings=input("Enter greetings:")
greetings=greetings.strip().lower()

if greetings.startswith("hello") :
    print("$0")
elif greetings.startswith("h"):
    print("$20")
else:
    print("$100")
