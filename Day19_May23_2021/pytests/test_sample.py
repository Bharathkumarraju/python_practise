import pytest
from sample import One

def test_add_two_integers():
    res = One(10, 20)
    result = res.add()
    assert result == 30

def test_add_two_strings():
    res= One("Hello", "hi")
    result = res.add()
    assert result == "Hellohi"

def test_multiply_two_strings():
    with pytest.raises(TypeError):
        res = One("Hi", "hello")
        res.multilply()

def test_if_one_values_is_string():
    res = One("hi", 3)
    result = res.multilply()
    assert result == "hihihi"

def test_multily_one_value_string_another_value_negative():
    with pytest.raises(ValueError):
        res = One("hi", -3)
        res.multilply()
def test_multiply_one_value_string_another_value_float():
    with pytest.raises(TypeError):
        res = One("hi", -3.5)
        res.multilply()
def test_multiply_for_two_integers():
    res = One(10, 18)
    result = res.multilply()
    assert result == 180

def test_add_one_is_string_another_is_int():
    res = One("hi",10)
    result = res.add()
    assert result == "hi10"

def test_multiply_two_neagative_integers():
    res = One(-9, -2)
    result = res.multilply()
    assert result == 18
