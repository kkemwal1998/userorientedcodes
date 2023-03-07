

from calculator import square


def main() :

    test_square()

def test_square() :

    assert square(2) == 4     # It sates that this particular function is definately true. Otherwise if something is wrong in our function, then there will be an assertion error in our code on terminal.
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
if __name__ == "__main__" :
    main() 

# We will be using pytest with the help of [ pip install pytest] on our terminal. We will be using pytest in order to automate our unit testing procedure on our code. It directly shows pass and fail on the terminal.