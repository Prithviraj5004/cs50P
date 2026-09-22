#meal timing and whats the meal depend upon user input
#1 ask user for input time
#2 convert the time into 24 hours clock
#3 make times for dinner,lunch,breakfast according to timeing given by user
#4 the output will depend on user input of time

import datetime

def main():
    time = input("Enter time:").strip()
    hours=convert(time)

    if 7.00 <= hours <= 8.00 :
        print("Breakfast time")
    elif 12.00 <= hours <= 13.00:
        print("Lunch time")
    elif 18.00 <= hours <= 19.00:
        print("Dinner time")
    else:
        print("")

def convert(time):
    hours , minutes=map(int, time.split(":"))
    return hours+minutes /60

if __name__== "__main__":
    main()
