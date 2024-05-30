from lib.make_snippet import *

# testing a function that takes a string as an arguement and returns the first five words and then a '...'

def test_snippet_returning_first_five():
    result = make_snippet('bananas')
    assert result == 'banan...'

def test_snippet_shorter_than_five():
    result = make_snippet('dog')
    assert result == 'dog...'

def test_snippet_no_text():
    result = make_snippet(' ')
    assert result == ' ...' 

def test_snippet_symbols():
    result = make_snippet('hi!')
    assert result == 'hi!...'