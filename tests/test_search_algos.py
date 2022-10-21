import pytest
from asd.generators import *
from asd.search_algos import binary_search, __binary_search__, ternary_search

def test_binary_search_edge_cases():
    with pytest.raises(RuntimeError):
        __binary_search__([], None, 0, 0)

    with pytest.raises(RuntimeError):
        __binary_search__([], 0, 0, 0)

    with pytest.raises(RuntimeError):
        __binary_search__([1], 1, 1, 0)

    with pytest.raises(RuntimeError):
        binary_search(None, None)

    with pytest.raises(RuntimeError):
        binary_search([], None)

    with pytest.raises(RuntimeError):
        binary_search(None, 1)


def test_binary_search_positive_no():
    v = array.array('I', [1, 3, 4, 7, 11])

    assert binary_search(v, 1,) == 0
    assert binary_search(v, 11) == 4
    assert binary_search(v, 3) == 1

def test_binary_search_negative_no():
    v = array.array('i', [-10, 0, 3, 4, 7, 11])

    assert binary_search(v, -10) == 0
    assert binary_search(v, 0) == 1

def test_ternary_search_edge_cases():
    with pytest.raises(RuntimeError):
        ternary_search(None, None)

    with pytest.raises(RuntimeError):
        ternary_search([], None)

    with pytest.raises(RuntimeError):
        ternary_search(None, 10)

def test_ternary_search():
    v = gen_vector_even(100)

    #first element
    assert ternary_search(v, 0) == 0

    #last element
    assert ternary_search(v, 198) == 99

    #middle element
    assert ternary_search(v, 100) == 50

    #left not found
    assert ternary_search(v, -100) == False

    #right not found
    assert ternary_search(v, 200) == False