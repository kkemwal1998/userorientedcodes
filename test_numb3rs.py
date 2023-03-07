




from numb3rs import validate

def main() :
    testing_IPformat() 
    test_word()

def testing_IPformat() :
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False

def test_word() :
    assert validate("cat") == False




if __name__ == "__main__":
    main()
