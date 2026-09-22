#pset chya website varun hint cha vapar kela ahe
#mumy chi madat ghetli pan sagla me lihila ahe

import sys
from pyfiglet import Figlet
figlet=Figlet()
fonts=figlet.getFonts()
import random


if len(sys.argv)==1:
    figlet.setFont(font=random.choice(fonts))

elif len(sys.argv) > 2 and sys.argv[1]=="-f":
        if sys.argv[2] in fonts:

            figlet.setFont(font=sys.argv[2])

        else:
            sys.exit("Invalid argument")


else:
    sys.exit("Invalid argument")

userinput = input("Enter a name with or without font:")
print(figlet.renderText(userinput))






