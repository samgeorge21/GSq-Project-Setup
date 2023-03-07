from lib.gratitudes import *

def test_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("Happiness")
    gratitudes.add("Health")
    assert gratitudes.format() == "Be grateful for: Happiness, Health"
    