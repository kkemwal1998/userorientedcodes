# We will be using the concept of dictionary into this one.
# We can also return our dictionary in python.
# 
def main() :
    student = get_student()
# In order to increase our consistency, we can use conditional statements. 
    if student["name"] == "Padma" :        # In the concept of dictionary, we use strings in order to index the values. 
        student["house"] == "Ravenclaw"    
    print(f"{student['name']} from  {student['house']}")   # We have used single quote in order to avoid any kind of confusion.
def get_student() :
    name = input("Name :")
    house = input("House :")
    return {"name": name, "house": house}     # In returning our dictionary, we will key values "name " and "house". And in front of them, we will be using our inputs for the same.
if __name__== "__main__" :
    main()