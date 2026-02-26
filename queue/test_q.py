from q import *
import pytest
def test_empty():
    empty = Queue()
    assert empty.isEmpty() is True

def test_add():
    q = Queue()
    q.add("A")
    assert q.head.data == "A"
    q.add("B")
    assert q.head.data =="A"
    next_node = q.head.next
    assert next_node.data == "B"

def test_size():
    q= Queue()
    q.add("A")
    assert q.size() == 1

def test_pop_left():
    q = Queue()
    q.add("A")
    q.add("B")
    
    item = q.pop_left()
    assert item == "A"
    assert q.size() == 1
    assert q.head.data == "B"


test_empty()
test_add()
test_size()
test_pop_left()
