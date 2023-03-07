

name = raw_input("What's your name?")      # We will assign the variable named name, which shall include the raw input of our VARIABLE.

file = open("names.txt", "a")     # We will assign the variable named file which will consist of the use of the open function. Under which, our file of names will be created which shall consist of our input. Also it will contain append so that an input does not get replaced and each new one is added to it.

file.write(name)           # This function will enable us to make somne kind of modifications in our input.
file.close()               # This function ensures that our file gets closed and does not get corrupted in future.

# After this, we will run our code on the terminal. Then we will type code names.txt in order to get access to our input.