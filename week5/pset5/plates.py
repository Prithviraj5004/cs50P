def main():
    plate = input("Plate: ").strip().upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    if not s.isalnum():
        return False


    first_digit_index = None
    for i, char in enumerate(s):
        if char.isdigit():
            first_digit_index = i
            break

    if first_digit_index is not None:
        if s[first_digit_index] == '0':
            return False
        if not all(char.isdigit() for char in s[first_digit_index:]):
            return False

    return True



if __name__ == "__main__":
    main()