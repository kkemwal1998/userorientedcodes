


# problem set


from fuel import convert,guage

import pytest

def main():
    test_convertandguage()

    test_number()

def test_convertandguage() :
    assert convert("4/9") == 44 and guage(44) == '44%'
    assert convert("3/6") == 50 and guage(50) == '50%'






def test_number():

    assert guage(0) == "E"
    assert guage(99) == "F"

    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    
    with pytest.raises(ValueError):
        convert("ram/dog")



if __name__ == "__main__":
    main()


