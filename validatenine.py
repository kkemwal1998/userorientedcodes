
# In this, we will be using the prgram thst is actually used by the google browser.

import re

email = input("What's your email ?").strip()

if re.search("^\w+@(\w+\.)?\w+\.(com|gov|org|edu)$", email, re.IGNORECASE) :    # Thus, our domain after the username will be represented by the  (\w+\.)?. Under which, ? will inly allow upto max 1 repetition of this domain in future.
    print("valid")
# But it still would not be able to deal with the problem of multiple @ in our string.
else :
    print("invalid")