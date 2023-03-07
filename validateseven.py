

# In this, we will be using square brackets to highlight the range of characters which could be integers, numbers, underscore or anything within our code and there is no requiement for any commas. We can use "-" for this.
# This pattern is majorly used in the forms. 
#[We can also replace square bracket method with \w which represent any word character or number.]
# In order to make our code more inclusive, we will parallel bars method for the end of string. That is a|b represents either a or b .
# In order to ignore uppercase or lowercase of the inputs, we will the function of flags that is already present there in our gores function of re.search .
import re

email = input("What's your email ?").strip()

if re.search("^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.(com|gov|org|edu)$", email, re.IGNORECASE) :    # Thus for the username and domain, we have used the square brackets to increase our inclusivity.
    print("valid")
# But it still would not be able to deal with the problem of multiple @ in our string.
else :
    print("invalid")
# Our program above is good but as we can see, we will not be able to accomodate multiple dots in an email adress. That is if we give our input as (kanishk@cvs.du.com), it will be considered invalid. Thus we will try to improve this code in our next program.