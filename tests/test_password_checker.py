import pytest 
from lib.password_checker import *

# when password isnt valid 

def test_password_isnt_valid():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check('five')
    message = str(e.value)
    assert message == ("Invalid password, must be 8+ characters.")