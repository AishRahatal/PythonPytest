
'''	
@Author: Aishwarya
@Date: 2021-12-1 
@Title :
'''
#########################################################################################
import pytest
from calc import Calculator

obj=Calculator()

def test_add():
    """
    Description:Test case function for addition
    Parameter: self
    Return: none
    """
    value = obj.add(4, 5)
    assert value == 9


def test_subtract():
    """
    Description:Test case function for subtratction
    Parameter: self
    Return: none
    """
    value = obj.sub(12,5)
    assert value == 7


def test_subtract_negative():
    """
    Description:Test case function for subtratction
    Parameter: self
    Return: none
    """
    value = obj.sub(4, 5)
    assert value == -1


def test_multiply():
    """
    Description:Test case function for multiplication
    Parameter: self
    Return: none
    """
    value = obj.mul(2,3)
    assert value == 6


def test_divide():
    """
    Description:Test case function for division
    Parameter: self
    Return: none
    """
    value = obj.div(8,4)
    assert value == 2

def test_divide_by_zero():
    """
    Description:Test case function for division by zero
    Parameter: self
    Return: none
    """
    with pytest.raises(ZeroDivisionError) as e:
        obj.div(10,0)
    assert "division by zero" in str(e.value)