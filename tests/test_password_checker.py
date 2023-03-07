import pytest
from lib.password_checker import PasswordChecker

def test_correct_password_check():
    password = PasswordChecker()
    assert password.check("Password") == True

def test_incorrect_pwlength():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("Passwor")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_pw_over_8():
    password = PasswordChecker()
    assert password.check("Passworddd") == True

def test_correct_password_int():
    password = PasswordChecker()
    assert password.check("12345678") == True