

A = input("Write file name:") # Write the name of mediafile Eg: cat
 # Write the type of mediafile Eg:.gif,.zip,.pdf,.txt,.png,.jpg,.jpeg


if  ".gif" in A :
    B = A.removeprefix(A)

    C = "image" + B +"/" + "gif"
    
    print(C)
elif  ".zip" in A :
    B = A.removeprefix(A)
    
    C = "application" +  B +"/" + "zip"


    print(C)

elif  ".PDF" in A :

    B = A.removeprefix(A)
   
    C = "application" +  B +"/" + "pdf" 

    print(C)

elif  ".txt"  in A :

    B = A.removeprefix(A)
    
    C = "txt" +  B +"/" 
    print(C)

elif  ".png" in A :

    B = A.removeprefix(A)
    
    C = "image" +  B +"/" + "png"
    print(C)
elif  ".jpg" in A :

    B = A.removeprefix(A)
    
    C = "image" +  B +"/" + "jpeg" 
    print(C)
elif  ".jpeg" in A :

    B = A.removeprefix(A)
    
    C = "image" + B +"/" + "jpeg"
    print(C)

elif ".pdf" in A :
    B = A.removeprefix(A)
   
    C = "application" +  B +"/" + "pdf" 

    print(C)




else :
    print("application/octet-stream")