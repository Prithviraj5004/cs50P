def main():
    user = input("Word: ")
    print(shorten(user))


def shorten(user):
    result = ""

    for letter in user:
        if letter.lower() not in ["a", "e", "i", "o", "u"]:
            result += letter

    return result


if __name__ == "__main__":
    main()