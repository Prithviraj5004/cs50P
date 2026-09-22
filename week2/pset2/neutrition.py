#1 ask user for input a fruit
#2 display the fruit calories
#3 ignore all the fruits other than the fruits on the list
# case sensitive(piece of cake)
#name must be same as on chart exa if bananas is on chart user should type bananas not only banana otherwise it will give error
user_input=input("Enter fruit name:")

if user_input.lower()=="apple":
    print("Calories:130")
elif user_input=="Avocado":
    print("Calories:50")
elif user_input=="Banana":
    print("Calories:110")
elif user_input=="Cantaloupe":
    print("Calories:50")
elif user_input=="Grapefruit":
    print("Calories:60")
elif user_input=="Grapes":
    print("Calories:90")
elif user_input=="Honeydew Melon":
    print("Calories:50")
elif user_input=="Kiwifruit":
    print("Calories:90")
elif user_input=="Lemon":
    print("Calories:15")
elif user_input=="Lime":
    print("Calories:20")
elif user_input=="Nectarine":
    print("Calories:60")
elif user_input=="Orange":
    print("Calories:80")
elif user_input=="Peach":
    print("Calories:60")
elif user_input=="pear":
    print("Calories:100")
elif user_input=="Pineapple":
    print("Calories:50")
elif user_input=="Plums":
    print("Calories:70")
elif user_input=="Strawberries":
    print("Calories:50")
elif user_input=="Sweet Cherries":
    print("Calories:100")
elif user_input=="Tangerine":
    print("Calories:50")
elif user_input=="Watermelon":
    print("Calories:80")
else:
    print("")
