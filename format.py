
# In this, we will be dealing the with the formating of user input data.

name = input("What's your name ?")

if "," in name :      # we are setting up the condition statement to ensure that the comma between the names get removed.
    last, first = name.split(", ")
    name = f"{first} {last}"

print(f"hello, {name}")

# But the only problem with the above programme is that if we write kanishk, kemwal in it then it well be not re-formated.