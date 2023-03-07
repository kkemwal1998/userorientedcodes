
# In this, we will be using parallel lines(|) in order to tighten our program. It becomes easier to read. 
name = input("What's your name ?")

match name:
    case "Harry"| "Hermoine" | "Ron" :
        print("Gryfindor")
    case "Draco" :
        print("Slytherin")

    case _:
        print("Who?")

    # Thus, this is the concept of our match function.