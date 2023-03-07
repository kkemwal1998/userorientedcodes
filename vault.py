

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self) :       # We are defining this str in order to make sure that our output is user firendly, we have to define string function.
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"


    def __add__(self,other) :     # Self represents left hand operator which is potter snf other represents right hand operator which is weasley.
        
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25,50,100)
print(weasley)

# If we use the below without operator overload:
#------------->total = potter + weasley
# ------------>print(total)
# It will not work. Thus we will be using operation overloader for this purpose under the class.

total = potter + weasley
print(total)

# Thus our code will work.