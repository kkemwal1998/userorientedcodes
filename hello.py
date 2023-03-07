def main():
    A = input("What's your name ?")
    hello(A)

def hello(n):
      
    return "hello, " + n 

    #print("hello, " + n)    ---------------> We could also use this but the unit tests functions only demand return of the values.  

if __name__ == "__main__" :   # This ensures that our hello function will get exported to to test_hello.py .
    main()