import pytest
from file import add, divide

import time 

def test_add():
    result = add(1, 4)
    assert result == 5

def test_divide():
    result = divide(10, 2)
    assert result == 5
    
    
def test_add_strings():
    result = add("i like ","burgers")
    assert result == "i like burgers"


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
     divide(10,0)
@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = divide(10,2)
    assert result == 5 
    
@pytest.mark.skip(reason="This feature is to skip")
def test_add():
    assert add(1,2)==3
    
@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_zero_broken():
    
    assert divide(10,0) 