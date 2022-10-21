import pytest

from asd.generators import *

def test_fibonacci():    
    assert gen_fibonacci(0) == array.array('d', [])
    
    v = gen_fibonacci(5)
    assert len(v) == 5
    assert v == array.array('d', [1.0, 2.0, 3.0, 5.0, 8.0])
    
def test_vector_even():
    assert gen_vector_even(0) == array.array('I')
    
    v = gen_vector_even(100)
    
    #first and last values
    assert v[0] == 0
    assert v[99] == 198
    
    #all elements are even
    for item in v:
        assert round(item % 2) == 0
        
def test_vector_odd():
    assert gen_vector_odd(0) == array.array('I')
    
    v = gen_vector_odd(100)
    
    #first and last values
    assert v[0] == 1
    assert v[99] == 199
    
    #all elements are odd
    for item in v:
        assert round(item % 2) == 1