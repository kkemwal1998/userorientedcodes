# We will further upgrade our program. We will be removing self argument and add class which is cls instead of that one.
# We will be a class method inside a class.

import random 

  
class Hat :
# We will eliminate our class object function with self argument. Then we will convert our program into class variable. 
    houses = ["Gryfindor", "Hufflepuff", "Ravenclaw", "Slytherin"]   # We have created a class variable  to include the list of houses. It can be made accesable to many functions.
    @classmethod
    def sort(cls,name) :

        house = random.choice(cls.houses) # We are creating this variable in a way that random house is picked when we pass in the name. Thus, we used random.choise for the same.
        print(name, "is in", house)

Hat.sort("Harry")


# After passing the function, the house with Name harry will be chosen randomly.
