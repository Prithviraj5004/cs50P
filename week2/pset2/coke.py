# coke vending machine(entirely aaai used but logic clear) bv
#1 display 50 cent as owed or money to be paid
#2 only accept 5,10,25 cent coins from user error otherwise
#3 when user insert coins subtract it from the ammount and display the remaning ammount and again ask for money to be insert
#4 if all the money is completed break


amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
        amount_due -= coin

print(f"Change Owed: {-amount_due}")