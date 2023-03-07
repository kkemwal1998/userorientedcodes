# Problem set

import sys
import requests
import json

try :
    A = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json' )

    B = A.json()
    C = B.get("bpi")
    D = C.get("USD")
    E = D.get("rate_float")
    amount = E*float(sys.argv[1])
    print(f"${amount:,.4f}")


except ValueError:
    print("command line argument is not number")
    sys.exit(1)

except IndexError :
    print("Missing command-line argument")
    sys.exit(1)



