

# Problem set
 

import sys



def main() :
    A = input("Input :")
    output = shorten(A)
    print(f"Output:{output}")

def shorten(word) :
    B = ["a","e","i","o","u"]
    C = ["A","E","I","O","U"]
    
    if word == word.lower() :
        for character in word  :
            if character in B   :
                word = word.replace(character,"")
                   
            

    elif word == word.upper() :
        for character in word :
            if character in C  :
                word = word.replace(character,"")

               
    elif word == word.capitalize() :
        for character in word  :
            if character in B   :
                word = word.replace(character,"")
            

    return word
    

if __name__ == "__main__" :
    main()