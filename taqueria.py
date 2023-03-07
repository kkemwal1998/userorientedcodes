# Problem set
# In this, for some reason cntrol-d shall be replaced by cntrol-z . Otherwise, EoF error will not be called and we will not get our total amount.
import sys
A = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
sum = 0
while True :
    try:
        B =  input("Item:")
        
        if B in A  :
            
            sum += A[B]
            continue
        
        else :              # The program will not work if our input is not in the dictionary.
            sys.exit()  
        
    except EOFError:
        print(f"Total:$",sum)
        
        continue
