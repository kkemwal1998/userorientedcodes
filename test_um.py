


from um import count


def main() :

    test_one_um()
    test_two_otherword()
    test_three_num()

def test_one_um() :

    assert count("hello, um") == 1
    assert count("Um, I Love you, um") == 2

def test_two_otherword() :
    assert count("hello") == "0"
    assert count("album") == "0"
    

def test_three_num() :
    assert count("3") == "0"


if __name__ == "__main__":
    main()