from os import lseek


def main():
    X = int(raw_input("What's X"))
    print("X squared is", square(X))

def square(n):
    return pow(n,2)
main()        