

# In this, we will amalgamate both get name and get house function under get student function. 
# ALso, in Python langauge we can return both values.

def main() :
    N,H = get_student()    # N and H stand for variables called name and house. 
    print(f"{N} from {H}")

def get_student() :
    N = input("Name: ")
    H = input("House: ")
    
    return N, H      # We can return both values in our python language.

if __name__ == "__main__" :      # As we did this earlier, it helps in importing our functions in future. 
    main()

# We could further improve our code by making use of tuple data in studentthird.py .