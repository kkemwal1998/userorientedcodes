
with open("names.txt", "r") as file :
    values = file.readlines()    # Since, our values are in a single line form in the file named names. Thus, we will make use of this readlines function for the same. This particular function reads all the lines in a file.
    
for line in values:                # We will add loop in order to make sure that each line in our file "names" gets printed with hello.
    print("hello,", line)