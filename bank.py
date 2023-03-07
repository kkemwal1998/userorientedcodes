










# problem set

def main() :
    A = input("Greetings:")
    R = value(A)
    print(f"${R}")

def value(greeting) :
    greeting = greeting.lower().strip()

    if greeting == "hello" :

        #print("$0")
        return 0

    elif greeting[0] == "h" :
        #print("$20")
        return 20

    else :
        #print("$100")
        return 100

if __name__ == "__main__":
    main()


