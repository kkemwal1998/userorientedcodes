

name = raw_input("What's your name?")      # We will assign the variable named name, which shall include the raw input of our VARIABLE.

with open("names.txt", "a") as file :    # We will be using with function in order to automtically open our file named "names" under the variable named file. Also it will contain append so that an input does not get replaced and each new one is added to it.

    file.write(name)           # We will indent this function in order to make sure that if an input is not provided, then the file shall get automatically closed. This function will enable us to make somne kind of modifications in our input.


# After this, we will run our code on the terminal. Then we will type code names.txt in order to get access to our input.