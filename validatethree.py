# now, I just want to make sure that there is .com at the end of string, we will use backlash (\) in order to separate within a string. Thus, backlash will ensure that we get only .com at the end.
# After implementing the function, we will get it as invalid.
import re 

email = input("What's your email?").strip()

if re.search(".+@.+\.com", email):        # Thus we will using ".+" syntax of the module to ensure that characteters are once repested which are before @ and after @ . If we use ".*" it will show that the character is either repeated or never repeated.
    print("valid")
# Thus, it can solve multiple problems.
else :
    print("invalid")


# Also, If we write our input as (my email is kanishk14kk@gmail.com), it will still show as valid. Thus, we want to avoid it because we want to ensure that our input as only email id to be considered as valid.