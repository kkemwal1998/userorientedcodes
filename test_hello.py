# In this, we have tested our hello function from the hello file.
from hello import hello

def test_hello():
    assert hello("Matt") == "hello, Matt"   # As usual, the assertion will ensure that our function's returned value is always true. Otherwise, our test will show some failure.
    assert hello("Hindu") == "hello, Hindu"
