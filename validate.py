# We can check the validity of user input by makaking use of string functions.

# we are required to set high bars so that the validity could properly be checked in a more presice manner.

email = input("What's your email ?").strip()  # We will be using strip function in order to make sure that there are no whitespaces.

username, domain = email.split("@")    # we will be using split fuction in order to ensure that "@" is isolated from the string.

if username and domain.endswith(".edu") :   # We shall be using endswith function of the string for checking the validity.
    print("valid")

else :
    print("invalid")

# As we can see, we can further improve our program, which we will do in the future.Because we have not added enough filters into this one.


