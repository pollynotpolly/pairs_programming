from lib.string_builder import *

#initally output is an empty string

def test_initial_string_output():
    string_builder = StringBuilder()   #file name of code followed  by class name
    assert string_builder.output() == ""  #see first line of code

#adds string 
def test_adds_to_string():
    string_builder = StringBuilder()
    string_builder.add("Conan")
    assert string_builder.output() == "Conan"
    
#when we add a single string the size reflects the size of that string

def test_length_of_string_added():
    string_builder = StringBuilder()
    string_builder.add("Conan")
    assert string_builder.size() == 5
    
#all mehtods are covered - now need to test behaviour of class - in which it adds strings 

def test_adds_multiple_strings():
    string_builder = StringBuilder()
    string_builder.add("Conan")
    string_builder.add("loves")
    string_builder.add("Polly")
    assert string_builder.size() == 15
