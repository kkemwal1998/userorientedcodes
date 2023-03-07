

# Problem set


import re



def main():

    O = input("Hours: ")
    R = convert(O)
    print(R)

def convert(s):
    A = re.search("^(1[0-2]|0?[1-9]):*([0-5][0-9])*.([A-P]M).to.(1[0-2]|0?[1-9]):*([0-5][0-9])*.([A-P]M)$",s)
       
    if  A :
        elements = A.groups()

        if int(elements[0]) <= 12 or int(elements[3]) <= 12 :

            if elements[2] == 'AM' and elements[5] == 'AM' :
                #print(s)
                D = s.replace('AM'," ")
                return D

            elif elements[2] == 'AM' and elements[5] == 'PM' :
                C = 12 + int(elements[3])
                D = '0' + str(elements[0]) + ':'+ str(elements[1]) + ' to ' + str(C) + ':' + str(elements[4]) 
                #print(D)
                return D

            elif elements[2] == 'PM' and elements[5] == 'PM' :
                E = 12 + int(elements[0])
                F = 12 + int(elements[3])
                G =  str(E)  + ':' + str(elements[1]) +  ' to ' + str(F) + ':' + str(elements[4])  
                #print(G)
                return G

            elif elements[2] == 'PM' and elements[5] == 'AM' :
                H = 12 + int(elements[0])
                I =  str(H) + ':'+ str(elements[1])  + ' to ' +'0' + str(elements[3]) + ':' + str(elements[4]) 
                #print(I)
                return I
            #print(elements)

            elif int(elements[1]) == None or int(elements[4]) == None :
        
                
                if int(elements[1]) < 60 and int(elements[4]) < 60 :
                    if elements[2] == 'AM' and elements[5] == 'AM' :
                        #print(s)
                        D = s.replace('AM'," ")
                        return D

                    elif elements[2] == 'AM' and elements[5] == 'PM'  :
                    
                        C = 12 + int(elements[3])
                        D = '0' + str(elements[0]) + ':'+ str(elements[1])  +  ' to ' + str(C) + ':' + str(elements[4]) 
                        #print(D)
                        return D

                    elif elements[2] == 'PM' and elements[5] == 'PM' :
                        E = 12 + int(elements[0])
                        F = 12 + int(elements[3])
                        G = str(E)  + ':' + str(elements[1])  +  ' to ' + str(F) + ':' + str(elements[4]) 
                        #print(G)
                        return G

                    elif elements[2] == 'PM' and elements[5] == 'AM' :
                        H = 12 + int(elements[0])
                        I = str(H) + ':'+ str(elements[1]) +" " + str(elements[2]) +  ' to ' +'0' + str(elements[3]) + ':' + str(elements[4]) 
                        #print(I)
                        return I
                else :
                    raise ValueError

            elif int(elements[1]) == None and int(elements[4]) == None :


                if int(elements[1]) < 60 and int(elements[4]) < 60 :

                    if elements[2] == 'AM' and elements[5] == 'AM' :
                        #print(s)
                        D = s.replace('AM', " ")
                        return s
                    elif elements[2] == 'AM' and elements[5] == 'PM' :
                        C = 12 + int(elements[3])
                        D = '0' + str(elements[0]) + ':'+ str(elements[1])  +  ' to ' + str(C) + ':' + str(elements[4]) 
                        #print(D)
                        return D
                    elif elements[2] == 'PM' and elements[5] == 'PM' :
                        E = 12 + int(elements[0])
                        F = 12 + int(elements[3])
                        G = str(E)  + ':' + str(elements[1]) +  ' to ' + str(F) + ':' + str(elements[4]) 
                        #print(G)
                        return G
                    elif elements[2] == 'PM' and elements[5] == 'AM' :
                        H = 12 + int(elements[0])
                        I = str(H) + ':'+ str(elements[1])  +  ' to ' + '0' + str(elements[3]) + ':' + str(elements[4]) 
                        #print(I)
                        return I

                else :
                    raise ValueError


        else :
            raise ValueError

    else :
        raise ValueError

    

if __name__ == "__main__":
    main()























































