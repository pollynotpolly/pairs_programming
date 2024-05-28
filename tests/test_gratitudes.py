from lib.gratitudes import *

def test_initial_gratitudes():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

def test_add_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("Peanut Butter")
    assert gratitudes.format() == "Be grateful for: Peanut Butter"

# time to test multiple gratitudes

def test_multiple_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("Peanut Butter")
    gratitudes.add("Dogs")
    gratitudes.add("Parks")
    assert gratitudes.format() == "Be grateful for: Peanut Butter, Dogs, Parks"