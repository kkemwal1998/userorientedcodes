
def main() :
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name() :
    A = input("Name: ")
    return A

def get_house() :
    B = input("House: ")
    return B

if __name__ == "__main__" :      # As we did this earlier, it helps in importing our functions in future. 
    main()

# We could further tighten our code by amalgmating the above two functions.
