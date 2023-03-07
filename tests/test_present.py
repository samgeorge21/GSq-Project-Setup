import pytest
from lib.present import Present

def test_wrap_unwrap_present():
    present = Present()
    present.wrap(27)
    assert present.unwrap() == 27

def test_unwrap_no_wrap():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_wrapped_already():
    present = Present()
    present.wrap(65)
    with pytest.raises(Exception) as e:
        present.wrap(99)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_wrap_already_wrapped_preserves_value():
    present = Present()
    present.wrap(57)
    with pytest.raises(Exception) as e:
        present.wrap(82)
    assert present.unwrap() == 57