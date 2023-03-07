

# In this, we would use the concept of square bracket with carrot [^], it will ensure the exclusion of that particular character within our string.


import re

email = input("What's your email ?").strip()

if re.search("^[^@]+@[^@]+\.com$", email) :    # @ in our [^] will ensure that our @ is not included again.
    print("valid")

else :
    print("invalid")

