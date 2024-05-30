from lib.high_value import *

def test_inital_values():
    high_value = HighValue(5, 57)
    assert high_value.value_first == 5
    assert high_value.value_second == 57

def test_get_highest():
    high_value = HighValue(39, 7)
    assert high_value.get_highest() == "First value is higher"
    high_value2 = HighValue(2, 98)
    assert high_value2.get_highest() == "Second value is higher"
    high_value3 = HighValue(6,6)
    assert high_value3.get_highest() == "Values are equal"

def test_add():
    high_value = HighValue(39, 7)
    high_value.add(5, "first")
    assert high_value.value_first == 44
    high_value.add(13,"second" ) 
    assert high_value.value_second == 20