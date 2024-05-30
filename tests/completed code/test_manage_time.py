# {{PROBLEM}} Function Design Recipe


## 1. Describe the Problem

# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text, 
# assuming that I can read 200 words a minute.


## 2. Design the Function Signature

# def manage_time(text):
# parameters = string containing words, time
# return value = float / num rperesenting reading time
# side effects = could round down or up 

## 3. Create Examples as Tests

# Make a list of examples of what the function will take and return._

# EXAMPLE

#if given a text of 200 words it will return reading of 1
# manage_time('..200..') => 1.0

#if given a text of 400 words it will return reading of 2
# manage_time('..400..') => 2.0


#if given a text of 300 words it will return reading of 1.5
# manage_time('..300..') => 1.5

#if given a text of empty words it will return an error
# manage_time('....') => "Cant estimate reading time for an empty text"


# Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

# After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
import pytest
from lib.manage_time import *

def test_manage_time_with_200():
    text = " ".join(["word" for i in range(0, 200)]) #list comprehension that creates a list consisting of the string "word" repeated 200 times
    #using join method to take all the "word" and concatenantes them in to a single string 
    result = manage_time(text) #result calls function created
    assert result == 1.0

def test_manage_time_with_200():
    text = " ".join(["word" for i in range(0, 400)])
    result = manage_time(text)
    assert result == 2.0

def test_manage_time_with_300():
    text = " ".join(["word" for i in range(0, 300)])
    result = manage_time(text)
    assert result == 1.5

def test_manage_time_with_no_text():
    with pytest.raises(Exception) as e:
        manage_time(" ")
        error_message = str(e.value)
        assert error_message == "Cant estimate reading time for an empty text"