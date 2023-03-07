
# In this, we would be  printing student names and their houses in a sorted manner. Since we are not mentioning any key in our sorting process, they will be automatically sorted in alphabatical manner. 
students = []    # we will be creating an empty list in order to make sure that the variable B is appended to them.

with open("students.csv") as file :
    for line in file:               # We will be making use of the loop function, so that the function gets executed for values in each line which has been put under the variable called  file.
        row = line.split()           # Since each line consists of the names of the students and thier house name. Thus, we will use split function the strings in each line. It will return two values in each line.
        B = row[0] +  "is in " + row[1]     # Now we want to mention on our terminal that those names in their particlar houses. Thus, we will extract the strings of each line in a row wise manner with the help of indexes method and attach them with the strings under variable B. 
        students.append(B)                            # Then, we will make use of append fiunction in order to make sure that the function that has been assigned under the variable B is added to an empty list. 

for student in sorted(students) :        # Thus, after ensuring that the function is added to the empty list of students. We will use sorted function in order to make sure that they are added in alphabaticall order. Then we will be using loop function in order to make sure that each line is sorted in the list. 
    print(student)          