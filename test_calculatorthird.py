# In this, we will be using pytest in order to automate our code as well as writing a new one for the same.

from calculator import square

def test_square() :

    assert square(2) == 4     
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9