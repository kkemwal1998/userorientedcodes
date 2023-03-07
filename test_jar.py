




# Pythen set

# In this, we are going to test our class Jar that we prevously createrd in our prevous program.

from jar import Jar


def test_init():
    cookies = Jar()
    assert cookies.capacity == 12

    cookies1 = Jar(4)
    assert cookies1.capacity == 4


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    cookies = Jar()

    cookies.deposit(4)
    assert cookies.size == 4

    cookies.deposit(3)
    assert cookies.size == 7


def test_withdraw():
    cookies = Jar()

    cookies.deposit(5)

    cookies.withdraw(2)

    assert cookies.size == 3












