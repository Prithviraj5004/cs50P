#sagla me lihila ahe almost correct ahe 45 min lagle or less than that
#total time <1 hour
import random
import sys
while True:
    try:
        n = int(input("Level:"))
        if n > 0:
            number = random.randint(1, n)
            print(number)
            while True:
                userin = int(input("Guess:"))
                if userin>0:
                    if userin < number:
                        print("Too small!")

                    elif userin > number:
                        print("Too large!")
                    else:
                        print("Just right!")
                        sys.exit()





    except ValueError:
        print()


