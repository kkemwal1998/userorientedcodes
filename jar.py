





# Problem set


class Jar:


    def __init__(self, capacity=12):
        if 0 >capacity : 
            raise ValueError("Capacity of jar cannot be negative")
        self.capacity__ = capacity              # Attribute
        self.Size__ = 0                               # Attribute
    def __str__(self):       
        
        D =  "🍪"* self.Size__
        return D


    def deposit(self, n):

        if self.capacity__ < n :
            raise ValueError("Our cookie deposits cannot be more than the capacity")
        self.Size__ += n



    def withdraw(self, n):
        if self.Size__ < n :
            raise ValueError("This amount of cookies cannot be removed ")
        self.Size__ -= n



    @property
    def capacity(self):
        V = self.capacity__


        return V
    @property
    def size(self):
        P = self.Size__
        return P





cookies  = Jar(9)                      # Capacity of jar
    
cookies.deposit(7)                 # Amount of cookies deposited
cookies.withdraw(2)                 # Amount of cookies that can be withdrawn           
print(cookies)
#    print(cookies.capacity)
#    print(cookies.size)











