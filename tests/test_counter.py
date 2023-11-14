from lib.counter import *

def test_counter_to_add():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."

def test_counter_to_add_five():
    counter = Counter()
    counter.add(10)
    assert counter.report() == "Counted to 10 so far."