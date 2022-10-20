import pytest
from asd.generators import *
from asd.search_algos import binary_search

def test_binary_search_edge_cases():
    with pytest.raises(RuntimeError):
        binary_search(None, 0, 0, 0)
        
    with pytest.raises(RuntimeError):
        binary_search([], None, 0, 0)
        
    with pytest.raises(RuntimeError):
        binary_search([], 0, 0, 0)
        
    with pytest.raises(RuntimeError):
        binary_search([1], 1, 1, 0)

def test_binary_search_positive_no():
    v = array.array('I', [1, 3, 4, 7, 11])

    assert binary_search(v, 1, 0, len(v) - 1) == 0
    assert binary_search(v, 11, 0, len(v) - 1) == 4
    assert binary_search(v, 3, 0, len(v) - 1) == 1

def test_binary_search_negative_no():
    v = array.array('i', [-10, 0, 3, 4, 7, 11])

    assert binary_search(v, -10, 0, len(v) - 1) == 0
    assert binary_search(v, 0, 0, len(v) - 1) == 1