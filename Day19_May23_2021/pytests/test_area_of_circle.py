import pytest
from math import pi
from area_of_circle import area_of_circle

def test_radius_is_zero():
    result = area_of_circle(0)
    assert result == 0

def test_radius_is_string():
    with pytest.raises(TypeError):
        area_of_circle("Hello")
        area_of_circle(5+6j)

def test_radius_is_negative():
    with pytest.raises(ValueError):
        area_of_circle(-10)

def test_radius_is_morethan_one():
    result1 = area_of_circle(5)
    result2 = area_of_circle(6)
    assert result1 == pi * 5 * 5
    assert result2 == pi * 6 * 6
