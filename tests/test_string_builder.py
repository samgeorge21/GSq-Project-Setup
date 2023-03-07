from lib.string_builder import *

def test_string_builder():
    string = StringBuilder()
    string.add("String")
    string.add("Builder")
    result = string.size()
    assert result == 13
    result = string.output()
    assert result == "StringBuilder"