






def main():
    A = input("Fraction:")
    R = convert(A)
    print(guage(R))


def convert(s) :

    while True :



        try :
            Q,P = s.split("/")
            nume = int(Q)
            den = int(P)

            fra = nume/den

            if  fra <= 1 :
                Per = int(fra * 100)
                return Per



            else :
                s = input("Fraction:")
                pass



        except (ValueError, ZeroDivisionError) :
            s = input("Fraction:")
            pass



def guage(R) :
    if R <= 1 :
        return "E"

    elif R >= 99 :
        return "F"

    else :
        D = str(R) + "%"
        return D


if __name__ == "__main__":
    main()

