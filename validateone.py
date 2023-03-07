# We will be importing re module into this function in order to make sure that our function validation of patterns is better.

import re

email = input("What's your email?").strip()

if re.search("@", email):
    print("valid")

else :
    print("invalid")

# As we can see, we have still inporoved our code but we need to further bolster it. only "@" sign cannot be used.