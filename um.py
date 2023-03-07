

# Problem set


import re



def main():

    W = input("Text: ")
    R = count(W)
    print(R)

def count(L):
    
    
    
    #if re.search("^\w*\w*$",L,re.IGNORECASE) :

     #   B = "0"
        #print(B)
     #   return B

    #if re.search("^\w*\w*$",L,re.IGNORECASE) :
    #   B = "0"
        #print(B)
    #    return B


    #if re.search("^\w*um*\w*$",L,re.IGNORECASE) :
    #    B = "0"
        #print(B)
    #    return B

    #if re.search("^\w*um$",L,re.IGNORECASE) :
    #    B = "0"
    #    return B

    #if re.search("^\w*um*$",L,re.IGNORECASE) :
    #    B = "0"
    #    return B
    
    #if re.findall("^um\s*$",L,re.IGNORECASE) :
    #    B = len(re.findall("^um\s*$",L,re.IGNORECASE))

    #    return B

    #if re.findall("^\sum\s*$",L,re.IGNORECASE) :
    #    B = re.findall("^\s*um\s*$",L,re.IGNORECASE) 
    #    return B



    #if re.findall(r"(um)\b", L,re.IGNORECASE )  :              
    #    A = len(re.findall(r"(um)\b", L,re.IGNORECASE ))


    #    return A
    
    
    A = len(re.findall(r"\b(um)\b", L,re.IGNORECASE ))
    return A

    #if re.findall(r"\b(um)", L,re.IGNORECASE )   :

    #    A = len(re.findall(r"\b(um)", L,re.IGNORECASE ))
        
    #    return A

    #if re.findall(r"\b(um)\b", L,re.IGNORECASE ) :
    #    A = len(re.findall(r"\b(um)\b", L,re.IGNORECASE ))
    #    return A

        


    


if __name__ == "__main__":
    main()



























