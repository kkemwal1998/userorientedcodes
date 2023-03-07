













import sys
from fractions import Fraction


def main():
    A = input("Fraction:")
    R = guage(A)
    print(R)
    sys.exit()
def guage(P) :

    while True :


        try :


            B = Fraction(P)

            D = B * 100
            M = int(D)
            Z = "E"
            Q = "F"
            if B.numerator < B.denominator and B.numerator !=0  :
                W = str(M) + "%"

                #print(W)
                return W

            elif  B.numerator >= 0   and  M <= 1:

                #print(Z)
                return Z


            elif B.numerator <= B.denominator and M <= 1:

                #print(Z)
                return Z


            elif B.numerator <= B.denominator and   M >= 99 :


                #print(Q)
                return Q


            else :


                B = Fraction(P)

                D = B * 100
                M = int(D)
                if B.numerator < B.denominator and B.numerator !=0  :
                    W = str(M) + "%"
                    #print(W)
                    return W


                elif  B.numerator == 0   and  M <= 1:

                    #print(Z)
                    return Z



                elif B.numerator <= B.denominator and   M >= 99 :
                    #print(Q)
                    return Q


        except (ValueError, ZeroDivisionError) :


            S = input("Fraction:")

            B = Fraction(S)

            D = B * 100
            M = int(D)
            Z = "E"
            Q = "F"
            if B.numerator < B.denominator and B.numerator !=0  :
                W = str(M) + "%"

                #print(W)
                return W

            elif  B.numerator == 0   and  M <= 1:

                #print(Z)
                return Z


            elif B.numerator <= B.denominator and M <= 1:

                #print(Z)
                return Z


            elif B.numerator <= B.denominator and   M >= 99 :
                #print(Q)
                return Q

            else :


                B = Fraction(S)

                D = B * 100
                M = int(D)
                if B.numerator < B.denominator and B.numerator !=0  :
                    W = str(M) + "%"
                   # print(W)
                    return W


                elif  B.numerator == 0   and  M <= 1:

                    #print(Z)
                    return Z



                elif B.numerator <= B.denominator and   M >= 99 :
                    #print(Q)
                    return Q



if __name__ == "__main__":
    main()

    # We have used continue so that we can go back to the top.

