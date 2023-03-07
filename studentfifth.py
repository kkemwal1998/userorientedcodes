# In this, we will be using class keyword in order to invent our data type which is called Student.


class Student: # In this, we will be using the keyword called class under which Student will act as a cintainer for costum names.
    ...          # These three dots insure that our whole function comes back to thye class whithout any kind of indentation block from main function.


def main() :
    student = get_student()
    print(f"{student.name} from {student.house}")   # We have used single quote in order to avoid any kind of confusion.

def get_student() :  # In our function, we will be replacing the dictionary with the classes. 
    student = Student()    # Student() is syntax which is used for creating an object of certian class .We will be equating the variable with the class Student. That is we are creating a student object.
    student.name = input("Name: ")     # We will be using dot (.) in case of class in order to make sure that we create inside attributes of the student which we will be equating to the user input. 
    student.house = input("House: ")    # Thus, name and housen will be our attributes, which can also be called instances variable.
    return student   # Get function is returning the student object.


    

if __name__== "__main__" :
    main()