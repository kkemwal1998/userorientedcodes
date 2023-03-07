# In this, we will be using match function which will act as our alternative to conditional statements.

name = input("What's your name ?")
# Under match function, multiple cases will be handeled under which, user inputs will be considered.
match name:
    case "Harry" :
        print("Gryfindor")

    case "Hermione" :
        print("Gryfindor")

    case "Ron" :
        print("Gryfindor")

    case "Draco" :
        print("Slytherin")

    case _:                  # The underscore(_) represents the blank which means that this case has not been handeled yet.
        print("Who?")    
 
 # We could further tighten our program by using parralell veertical line(|). They represent  or statement in match function.  