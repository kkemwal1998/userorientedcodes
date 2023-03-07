





import sys



B = "Amount Due : 50"
print(B)

while True :
            

    try :
        Z = input("Insert Coin :")
        A = ["5","10","25"]

        if Z in A  :
            D = int(Z)
            
            A = 50- D
            E = A - D
            F = E - D
            H = F - D
            K = H - D
            X = K - D
            y = X - D
            N = y - D
            M = N - D
            O = M - D
            P = O - D
            print(f"Amount Due : {A}")
            if A != 0 :
                
            
                D = int(input("Insert Coin :"))
                E = A - D
                print(f"Amount Due : {E}")
            
            if E > 0 :
            
            
                D = int(input("Insert Coin :"))
                F = E - D
                print(f"Amount Due : {F}")
            
            else :
                print(f"Change Owed : {E}")
                sys.exit()
            if F > 0 :
            
            
                D = int(input("Insert Coin :"))
                H = F - D
                print(f"Amount Due : {H}")
            else :
                print(f"Change Owed : {F}")
                sys.exit()
            if H > 0 :

            
                D = int(input("Insert Coin :"))
                K = H - D
                print(f"Amount Due : {K}")
            else :
                print(f"Change Owed : {H}")
                sys.exit()
            if K > 0 :
            
            
                D = int(input("Insert Coin :"))
                X = K - D
                print(f"Amount Due : {X}")
            else :
                print(f"Change Owed : {K}")
                sys.exit()
            if X > 0 :
                D = int(input("Insert Coin :"))
                y = X - D
                print(f"Amount Due : {y}")
            else :
                print(f"Change Owed : {X}")
                sys.exit()
            if y > 0 :
                D = int(input("Insert Coin :"))
                N = y - D
                print(f"Amount Due : {N}")
            else :
                print(f"Change Owed : {y}")
                sys.exit()
            if N > 0 :
                D = int(input("Insert Coin :"))
                M = N - D
                print(f"Amount Due : {M}")
            else :
                print(f"Change Owed : {N}")
                sys.exit()
            
            if M > 0 :
                D = int(input("Insert Coin :"))
                O = M - D
                print(f"Amount Due : {O}")
            else :
                print(f"Change Owed : {M}")
                sys.exit()
            if O > 0 :
                D = int(input("Insert Coin :"))
                P = O - D
                print(f"Amount Due : {O}")

            else :
                print(f"Change Owed : {O}")
                sys.exit()
            
        else :
            print(B)


    except ValueError :
        continue        
        
            







    

