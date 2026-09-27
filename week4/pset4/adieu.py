
name_list = []

def main():
    while True:
        try:
            name = input("Name: ").strip()
            name_list.append(name)
        except EOFError:
            sound_of_music()
            return False


def sound_of_music():
    print("")
    if len(name_list) >= 2:
        new_s = ", ".join(name_list[0:-1])
        if len(name_list) == 2:
            print("Adieu, adieu, to " + new_s + " and " + name_list[-1])
        else:
            print("Adieu, adieu, to " + new_s + ", and " + name_list[-1])

    if len(name_list) == 1:
        print("Adieu, adieu, to " + name_list[0])


main()
