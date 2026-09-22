# bitcoin related question
#1 hour 20 min
#try to did but gave up after 30 min

import requests
import sys
if len(sys.argv)<2:
    sys.exit("Missing command line argument")
try:

        x = float(sys.argv[1])
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=2c44fe1cb8971b1c75c7f2749bb055d67950e793cd9045d9dc78d7a9807df123" )
        priceusd = response.json()
        print(priceusd)
        price=float(priceusd["data"]["priceUsd"])
        ammount=price*x
        print(f"${ammount:,.4f}")



except ValueError:
    sys.exit("Command line argument must be a number")





