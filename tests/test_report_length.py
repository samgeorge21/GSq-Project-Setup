from lib.report_length import *

def test_report_length():
    result = report_length("We are coding")
    assert result == "This string was 13 characters long."
    result = report_length("Makers")
    assert result == "This string was 6 characters long."