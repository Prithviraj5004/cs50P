#1 ask user for input
# check if input is 42 or forty-two or forty two
# if yes print yes
#else print no

user=input("Enter string you want to insert:")
user=user.strip()
if user=="42":
    print("Yes")
elif user=="forty_two":
    print("Yes")
elif user=="forty-two":
    print("Yes")
elif user=="forty two":
    print("Yes")
elif user=="Forty two":
    print("Yes")
elif user=="FoRty TwO":
    print("Yes")

else:
    print("No")


