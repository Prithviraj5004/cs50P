#ha sagla code ai ni kela ahe



def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            x, y = map(int, fraction.split('/'))

            if y == 0:
                raise ZeroDivisionError
            if x < 0 or x > y:
                raise ValueError

            percentage = (x / y) * 100
            rounded_percentage = round(percentage)

            if rounded_percentage <= 1:
                print("E")
            elif rounded_percentage >= 99:
                print("F")
            else:
                print(f"{rounded_percentage}%")
            break

        except (ValueError, ZeroDivisionError):
            continue

if __name__ == "__main__":
    main()