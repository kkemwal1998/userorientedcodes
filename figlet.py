# problem set
import sys
import random


import pyfiglet 



if len(sys.argv) == 1 :
    A = input("Input :")
    C = pyfiglet.FigletFont.getFonts()   # This is our list of fonts.

    B = pyfiglet.figlet_format(A, font= random.choice(C)) 
    print(f"Output : {B}")


elif len(sys.argv) == 3   :
    
    if sys.argv[1] == '-f' or '--font' :
        A = input("Input :")
        C = pyfiglet.FigletFont.getFonts()   # This is our list of fonts.

        if sys.argv[2]  in C :
                    

            D = pyfiglet.figlet_format(A, font= sys.argv[2])
            print(f"Output : {D}")

        else :
            
            sys.exit(" Invalid usage")
        

    else :
        sys.exit(" Invalid usage")
        



    
else :
    
    sys.exit(" Invalid usage")

    
