# In this, we will be adding the keyword called raise in order to make sure that a warning is given to programmer if a particular condition is not met.


class Student: # In this, we will be using the keyword called class under which Student will act as a cintainer for costum names.
    def __init__(self, name, house) :     # We mainly use init function in order to initialise the contents of the empty object under the class. Also, it helps in putting the variables in the object and adding values to them.
    
        if not name :
            raise ValueError("Missing name")      # In this, we have used a raise keyword in order to make sure that waring is given to the programmer if a particular condion is not met.
        if house not in ["Gryfindor", "Hufflepuff", "Ravenclaw", "Slytherin"] :     # If we want particular inputs, we have to create the list.
            raise ValueError("Invalid House")

        
        self.name = name         # As usual, we use dot in order to add new attributes.
        self.house = house

def main() :
    student = get_student()
    print(f"{student.name} from {student.house}")   

def get_student() :  # In our function, we will be replacing the dictionary with the classes. 

    name = input("Name: ")     # We will be using dot (.) in case of class in order to make sure that we create inside attributes of the student which we will be equating to the user input. 
    house = input("House: ")    # Thus, name and housen will be our attributes, which can also be called instances variable.
    student = Student(name, house)    # We will be equating the variable with the class Student. That is we are creating a student object.
    return student   # Get function is returning the student object.


    

if __name__== "__main__" :
    main()