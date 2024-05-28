from lib.check_codeword import *

## to check if codeword is correct

def test_with_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."
    
## to check if codeword is close

def test_with_close_codeword():
    result = check_codeword("hose")
    assert result == "Close, but nope."

## to check if codeword is wrong

def test_with_wrong_codeword():
    result = check_codeword("banana")
    assert result == "WRONG!"