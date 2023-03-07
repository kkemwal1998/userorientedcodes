# In this, we will be using the concept of inheritance. It is like drawing a family tree.


class Wizard :              # This will be our parent class.
    def __init__(self,name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

# We will refer to below class as child class.
class Student(Wizard):                                         # Now, there can be possibity that a student might be a wizard. Thus, We shall import the wizard with the help of inheritance.                                   
    def __init__(self, name, house):                                
        super().__init__(name)                                      # Since we are importing the class, we will eradicate the self.name . And, we will be replacing self.name with syntax called super() which shall provide acces to self.name in our init function.
        self.house = house
    ...

# We will refer to below class as child class.
class Professor(Wizard):                       # Now, there can be possibity that a proffesor might be a wizard. Thus, We shall import the wizard with the help of inheritance.
    def __init__(self, name, subject):
        super().__init__(name) 
        self.subject = subject
    ...

wizard = Wizard("Albus")       # This variable  shall take agrument underf class as "Albus".
student = Student("Harry")
professor = Professor("Severous")