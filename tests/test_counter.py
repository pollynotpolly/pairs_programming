from lib.counter import *

#initially roprts ount of zero

def test_counter_initally_reports_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

#when we add a single number to counter its reflected in final count

def test_counter_adds_a_single_number_to_the_count():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."

# so far we"ve only tested methods - not the full behaviour of the class 
# does it work when we add multiple numbers to the counter

def test_counter_adds_multiple_numbers_to_count():
    counter = Counter()
    counter.add(3)
    counter.add(6)
    assert counter.report() == "Counted to 9 so far."