# We are currently coming up with a program which will prompt the user to write the name of harry potter characters which will promptb the user to write the names of their houses.

# we will consolidate the conditional statements of the codes that print Gryfindor.
name = input("What's your name ?")

if name == "Harry" or name == "Hermione" or name == "Ron" :
    print("Gryfindor")

elif name == "Draco" :
    print("Slytherin")

else :
    print("Who?")  

# Thus, we could get rid of our code by using match function which will act as an alternative to our conditional statements in our code.