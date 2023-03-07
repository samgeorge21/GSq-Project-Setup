from lib.counter import *

def test_counter_class():
    counter = Counter()
    counter.add(5)
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 15 so far."