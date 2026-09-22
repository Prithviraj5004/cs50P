#sagla chapla ahe
#thoda me kela ahe
import inflect

p = inflect.engine()

def main():
    sing()

def sing():
    names = []
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        print("Adieu, adieu, to", p.join(names))

if __name__ == "__main__":
    main()