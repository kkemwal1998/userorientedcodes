# problem set

import sys
from random import randint


while True :
    try :  
        B = int(input("Level :"))
        if B > 0 :
            break
    except :
        pass


A = randint(1,B)      # This will avoid randint in our looping process.



while True :
    
    try :
        
        C = int(input("Guess :"))
        
        
    
        if A > C and C > 0 :
            print("Too small!")
            continue
        if A < C and C > 0 :
            print("Too large!")
            continue
        if A == C :
            print("Just right!")
            sys.exit()
        elif C < 0 :
            continue
    except ValueError :
        if C != int  :
            continue
       
    