

with open("students.csv") as file :
    for line in file:               # We will be making use of the loop function, so that the function gets executed for values in each line which has been put under the variable called  file.
        row = line.split()           # Since each line consists of the names of the students and thier house name. Thus, we will use split function the strings in each line. It will return two values in each line.
        B = row[0] +  "is in " + row[1]     # Now we want to mention on our terminal that those names in their particlar houses. Thus, we will extract the strings of each line in a row wise manner with the help of indexes method and attach them with the strings under variable B. 
        print(B)                            # Then, it will be printed on loop basis for each line.