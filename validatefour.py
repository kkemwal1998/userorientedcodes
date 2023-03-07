# We want to ensure that user input matches the start as well as end of the pattern. For this, we will use carrot and dollar feature.

import re 

email = input("What's your email?").strip()

if re.search("^.+@.+\.com$", email):        # Thus we will add ^ and $ in order to ensure that our starting and ending pattern with the user input. 
    print("valid")
# Thus, it can solve multiple problems.
else :
    print("invalid")

# But if we write kanishk@@@@@gmail.com, it will still show valid. Thus we will further imporve our code in validatefive.py .