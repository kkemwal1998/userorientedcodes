# We should know that we can create a function with the help of class.
# We will create a file uner which we will implement a function called class hat, which will sort the house as per the name of the student. That is, when a student name is passed, it shall the output the house.
import random 


class Hat :

    def __init__(self) :     # We will create a list of houses by defining  init function which only considers self as the argument. Thus we initiated the instance variables.
        self.houses = ["Gryfindor", "Hufflepuff", "Ravenclaw", "Slytherin"]   # We will be creating an instance variable to include the list of houses.
 
    def sort(self,name) :

        house = random.choice(self.houses) # We are creating this variable in a way that random house is picked when we pass in the name. Thus, we used random.choise for the same.
        print(name, "is in", house)

hat = Hat()
hat.sort("Harry")

# After passing the function, the house with Name harry will be chosen randomly.