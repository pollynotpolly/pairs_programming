import pytest
from lib.check_sentence_grammar import *

def test_check_sentence_grammar_capital_letter_and_fullstop():
    result = check_sentence_grammar("Lets go to the park and play with dogs.")
    assert result == True

def test_check_sentence_grammar_capital_letter_and_questionmark():
    result = check_sentence_grammar("Can we go to the park and play with dogs?")
    assert result == True

def test_check_sentence_grammar_capital_letter_and_exclamation():
    result = check_sentence_grammar("Lets go to the park and play with dogs!")
    assert result == True

def test_check_sentence_grammar_capital_letter_and_comma():
    result = check_sentence_grammar("Lets go to the park and play with dogs,")
    assert result == False

def test_check_sentence_grammar_no_capital_but_full_stop():
    result = check_sentence_grammar("let's go to the park and play with dogs.")
    assert result == False

def test_check_sentence_grammar_no_capital_but_questionmark():
    result = check_sentence_grammar("can we go to the park and play with dogs?")
    assert result == False

def test_check_sentence_grammar_no_capital_but_full_stop():
    result = check_sentence_grammar("let's go to the park and play with dogs!")
    assert result == False


def test_check_sentence_grammar_no_punctuation():
    result = check_sentence_grammar("Let's go to the park and play with dogs")
    assert result == False

def test_check_sentence_grammar_missing_both():
    result = check_sentence_grammar("let's go to the park and play with dogs")
    assert result == False

def test_check_sentence_grammar_no_text():
    with pytest.raises(Exception) as e:
        check_sentence_grammar(" ")
        error_message = str(e.value)
        assert error_message == "No text to check"

