


# Problem set :

from twttr import shorten


def main() :
    test_shorten()

def test_shorten():

    assert shorten("car") == "cr"
    assert shorten("CAR") == "CR"
    assert shorten("24") == "24"
    assert shorten("Car") == "Cr"
    assert shorten("cAR") == "cAR"
    assert shorten("hello") == "hll"

if __name__ == "__main__":
    main()      







