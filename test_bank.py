
# problem set

from bank import value

def main() :
    test_hello()
    test_alphabet ()
    test_otherthangreetings()


def test_hello():
    assert value("hello") == 0

def test_alphabet () :
    assert value("H") == 20

def test_otherthangreetings() :
    assert value("apple") == 100





if __name__ == "__main__":
    main()





