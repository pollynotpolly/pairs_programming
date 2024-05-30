from lib.count_words import *

# write test to check function that counts words in string and returns number

def test_counting_words_returning_num():
    result = count_words('I love dogs')
    assert result == 11

def test_counting_no_words():
    result = count_words("")
    assert result == 0

