import math
import pytest
import time

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius: int) -> None:
        self.radius = radius

    def area(self) -> int:
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> int:
        return  2 * math.pi * self.radius
    
class Rectangle(Shape):
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            return False
        return ((other.length == self.length) and (
                other.width ==  self.width)) or (
                (other.length == self.width) and (
                other.width == self.length))

    def area(self) -> int:
        return self.length * self.width

    def perimeter(self) -> int:
        return (2 * self.length) + (2 * self.width)

class Square(Rectangle):
    def __init__(self, sideLen: int):
        super().__init__(sideLen, sideLen)

def add(a, b):
    return a + b

def divide(a, b):
    return a/b

def test_add():
    assert add(2, 3) == 5

def test_add_fail():
    assert add(2, 3) == 4

def test_add_str():
    assert add('i like', ' burgers') == 'i like burgers'

def test_add_str_fail():
    assert add('i', 'like') == 'i like'

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def modified_division(a, b):
    if b == 0:
        raise ValueError
    return a/b

def test_mod_div():
    with pytest.raises(ZeroDivisionError):
        modified_division(10, 0)

class TestCircle:
    def setup_method(self, method):
        self.circle = Circle(10)
    
    def teardown_method(self, method):
        del self.circle
    
    def test_area(self):
        val = math.pi * self.circle.radius ** 2
        assert self.circle.area() == val

    def test_perimeter(self):
        val = 2 * math.pi * self.circle.radius
        assert self.circle.perimeter() == val

@pytest.fixture
def myRect():
    return Rectangle(10, 20)

@pytest.fixture
def oRect():
    return Rectangle(5, 6)

def test_area(myRect):
    val = 10 * 20
    assert myRect.area() == val

def test_perimeter(myRect):
    val = (2 * 10) + (2 * 20)
    assert myRect.perimeter() == val

def test_not_eq(myRect, oRect):
    assert not myRect.__eq__(oRect)

@pytest.mark.slow
def test_v_slow():
    time.sleep(5)
    assert divide(10, 2) == 5

@pytest.mark.skip(reason='Feature broken')
def test_add_broken():
    assert add(1, 2) == 3

@pytest.mark.xfail(reason='Cannot divide by zero')
def test_divide_break():
    divide(4, 0)

@pytest.mark.parametrize('sideLen, expected', [(5, 25), (3, 9), (10, 100), (9, 81)])
def test_mult_square_area(sideLen, expected):
    assert Square(sideLen).area() == expected

@pytest.mark.parametrize('sideLen, expected', [(3, 12), (5, 20), (9, 36), (10, 40)])
def test_mult_sqr_perimeter(sideLen, expected):
    assert Square(sideLen).perimeter() == expected

import service #method being mocked must be in another file
import unittest.mock as mock
import requests

@mock.patch('service.get_user_from_db') #path to method being tested
def test_get_user(mock_get_user):
    mock_get_user.return_value = 'Mocked Alice'
    user_name = service.get_user_from_db(1)
    
    assert user_name == 'Mocked Alice'

@mock.patch('requests.get') #path to method being tested
def test_get_user_api(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'id': 1, 'name': 'John Doe'}
    mock_get.return_value = mock_response
    data = service.get_users()
    assert data == {'id': 1, 'name': 'John Doe'}

@mock.patch('requests.get') #path to method being tested
def test_get_user_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    
    with pytest.raises(requests.HTTPError):
        service.get_users()