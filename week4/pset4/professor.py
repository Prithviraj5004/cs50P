#lihila mich ahe pan chai gapt is madad ghetli
#approx time 45-60 min
#total 1  hour



import random


def main():
    level = get_level()
    score=0

    for i in range(10):
        x=generate_integer(level)
        y=generate_integer(level)
        for attempt in range(3):
            try:
                ans=int(input(f"{x} + {y} ="))

                if ans== x+y:
                    score+=1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(x+y)

    print("Score:",score)




def get_level():
    while True:
        try:
            lvl = int(input("Level:"))
            if lvl in [1,2,3]:
                return lvl


        except ValueError:
            pass


def generate_integer(level):
    if level==1:
        return random.randint(0,9)
    elif level==2:
        return random.randint(10,99)
    elif level==3:
        return random.randint(100,999)



if __name__ == "__main__":
    main()