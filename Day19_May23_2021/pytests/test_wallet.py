"""
"""

import pytest
from wallet import Wallet

@pytest.fixture(scope="module")
def get_balance():
    print("Fixture is getting called")
    balnce = Wallet(100)
    return balnce

def test_get_the_current_balance(get_balance):
    assert get_balance.get_curret_balance() == 100
    assert isinstance(get_balance.get_curret_balance(), int) or isinstance(get_balance.get_curret_balance(), float)

@pytest.mark.parametrize("add_bal", [10, 20, 10.5, 20.5])
def test_add_to_the_current_balance(get_balance, add_bal):
     initial_bal = get_balance.get_curret_balance()
     get_balance.add_current_balance(add_bal)
     current_bal = get_balance.get_curret_balance()
     assert add_bal == current_bal - initial_bal
#     assert get_balance.add_current_balance(add_bal) == get_balance.add_current_balance(initial_bal)


@pytest.mark.parametrize("minus_bal", [10, 11, 10.5, 11.5])
def test_remove_from_the_current_balance(get_balance, minus_bal):
    initial_bal = get_balance.get_curret_balance()
    get_balance.subtract_current_balance(minus_bal)
    current_bal = get_balance.get_curret_balance()
    assert minus_bal == initial_bal - current_bal

def test_subtract_higher_value_from_current_balance(get_balance):
    with pytest.raises(ValueError):
        get_balance.subtract_current_balance(200)

def test_initial_balance():
    with pytest.raises(ValueError):
        initial_bal = Wallet(-100)


@pytest.mark.parametrize("neg", [(-5), (-6.5)])
def test_adding_negative_ints_floats(get_balance, neg):
    with pytest.raises(ValueError):
        get_balance.add_current_balance(neg)

@pytest.mark.parametrize("neg", [(-10), (-11.5)])
def test_removing_negative_ints_floats(get_balance, neg):
    with pytest.raises(ValueError):
        get_balance.subtract_current_balance(neg)


