from lib.greet import *

def test_greet():
    result = greet("Chris")
    assert result == "Hello, Chris!"