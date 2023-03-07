
# problem set
# In this, for some reason cntrol-d shall be replaced by cntrol-z . Otherwise, EoF error will not be called and we will not get our total amount.
import sys
A = {}

while True :
    
    try :
        B = input()
    
        # We will do the increment under if condition statement that is descerte increase.
        if B in A :
            A[B] += 1   
            
        else :
            A[B] = 1
            

    except EOFError :
        for food in sorted(A.keys()) :
            print(A[food],food.upper())
        sys.exit()
