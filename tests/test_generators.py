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
