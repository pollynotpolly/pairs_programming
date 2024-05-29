from lib.make_snippet import *

# testing a function that takes a string as an arguement and returns the first five words and then a '...'

def test_snippet_returning_first_five():
    result = make_snippet('bananas')
    assert result == 'banan...'