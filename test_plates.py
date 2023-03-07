

# Python set


from plates import is_valid

def main() :

    test_numwords()
    test_words()
    test_decimal()

def test_numwords():
    
    assert is_valid("aa2aaa") == True

    
def test_words() :
    
    assert is_valid("Hello") == True
    assert is_valid("goodbye") == False

def test_decimal() :

    assert is_valid("PR.34")  == False


if __name__ == "__main__":
    main() 















