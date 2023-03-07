# In this, we will be using the method which will recognise the pattern of multiple dots in the email address in our user input.
# The sign of ?  will mean 0 or 1 repetition at maximum and add prenthesis in order to seperate both of them. But if we have more than one dots then we will use star * in that case.
# Thus, it will recognise the case of one dot and more than one dots. Also, perenthesis plays a major role in highlighting the characters.
import re

email = input("What's your email ?").strip()

if re.search("^\w+@(\w+\.)?\w+\.(com|gov|org|edu)$", email, re.IGNORECASE) :    # Thus, our domain after the username will be represented by the  (\w+\.)?. Under which, ? will inly allow upto max 1 repetition of this domain in future.
    print("valid")
# But it still would not be able to deal with the problem of multiple @ in our string.
else :
    print("invalid")
# We coud remove further resriction that we will do in our code named validatenine.py