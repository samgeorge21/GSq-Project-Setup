from lib.check_codeword import *

def test_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."
    result = check_codeword("house")
    assert result == "Close, but nope."
    result = check_codeword("pancake")
    assert result == "WRONG!"
    result = check_codeword("holiday")
    assert result == "WRONG!"
    result = check_codeword("mouse")
    assert result == "WRONG!"

