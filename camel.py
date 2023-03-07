
import re 


ABC = input("camelCase:")
if ABC == ABC.lower() :
    print(f"snake_case:{ABC}") 


elif ABC != ABC.islower() :
    B = re.split('(?=[A-Z])', ABC)
    

    for F in B[1:] :
    

        D =  F.lower()

    X = B[0]+ "_" + D

    print(f"snake_case:{X}")

        
                
    
       
    
