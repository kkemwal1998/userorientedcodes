# we will make further changes in re search moodule, because if we only write @ or kanishk@, it will still show valid.

import re

email = input("What's your email?").strip()

if re.search(".+@.+", email):        # Thus we will using ".+" syntax of the module to ensure that characteters are once repested which are before @ and after @ . If we use ".*" it will show that the character is either repeated or never repeated.
    print("valid")
# Thus, it can solve multiple problems.
else :
    print("invalid")

# If we write kanishk@gmail?com, it will still show valid. Thus we will have to make few changes