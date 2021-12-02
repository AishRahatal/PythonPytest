
'''	
@Author: Aishwarya
@Date: 2021-12-1 
@Title :
'''
#########################################################################################
import pytest
from User import User_info

obj=User_info()


#positive test cases
def test_firstname():
    """"
    Description: this function test firstname
    Parameter: 
    Return: None
    """
    obj.validateName = 'John'
    assert obj.validateName=='John'
    

def test_lastname():
    """"
    Description: this function test  lastname
    Parameter: 
    Return: None
    """
    obj.validateName = 'Doe'
    assert obj.validateName=='Doe'

def test_email():
    """"
    Description: this function  test  email
    Parameter: 
    Return: None
    """
    obj.validateEmail="johndoe@yahoo.com"
    assert obj.validateEmail=="johndoe@yahoo.com"

def test_phone():
    """"
    Description: this function test  phone
    Parameter: 
    Return: None
    """
    obj.validatePhone="+919922445733"
    assert obj.validatePhone== "+919922445733"

def test_password():
    """"
    Description: this function test  phone
    Parameter: 
    Return: None
    """
    obj.validatePassword="Sqwe123#df"
    assert obj.validatePassword=="Sqwe123#df"   
