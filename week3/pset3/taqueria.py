#given dictnory of menus with there prices
#1 ask user for input of the menu
#2 add .lower to eliminate the captial eroor
#3 display the output prices with dollar sign at the end
#sagla chapla ahe
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0.0
    while True:
        try:
            item = input("Item: ").title()
            if item in menu:
                total += menu[item]
                print(f"Total: ${total:.2f}")
        except EOFError:
            break

if __name__ == "__main__":
    main()