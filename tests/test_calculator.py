'''My Calculator Test'''
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test that multiplication works '''
    assert multiply(2,2) == 4

def test_division():
    '''Test that division works '''
    assert divide(2,2) == 1

def test_divideByZero():
    '''Test divide by zero exception'''
    assert divide(2,0) 