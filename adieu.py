
# problem set



import sys


import keyboard
import inflect


L = inflect.engine()
F = []



while True :
    
    try :
        A = input("Name :")
        
        
        F.append(A)  
                  



    except EOFError :
       print("Name") 
       break








Line = L.join(F)

print("Adieu, adieu, to "  + Line)

