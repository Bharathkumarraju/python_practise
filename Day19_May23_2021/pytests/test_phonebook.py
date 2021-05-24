import pytest

from phonebook import Phonebook

"""
pytest fixtures: The test case will indicate that it needs some kind of resource (or) test fixture by specifying arguments to the test function.
pytest will then go and look for a function decorated with the "@pytest.fixture" decorator, and it should have the same name as the resource the test is requesting.
"""
# Now i want to modify my test fixture so that it will call the clear at the end of each test case.
# The way to do that is to replace the return statement with the "yield" statement.
# That means i can put some code after the yield statement that we run after each test case that uses this resource.

@pytest.fixture()
def phonebook(tmpdir):
    "Provides an empty phonebook"
    return Phonebook(tmpdir)
#    phonebook = Phonebook(tmpdir)
#    yield phonebook
#    phonebook.clear()
#    phonebook.clear()

def test_lookup_by_name(phonebook):
#    phonebook = Phonebook()
    phonebook.add("Bob", "1234")
    assert "1234" == phonebook.lookup("Bob")

def test_phonebook_contains_all_names(phonebook):
#    phonebook = Phonebook()
    phonebook.add("Bob", "1234")
#    assert phonebook.names() == {"Bob", "Missing"}
    assert "Bob" in phonebook.names()

def test_missing_name_raises_error(phonebook):
#    phonebook = Phonebook()
#    phonebook.add("Bob", "1234")
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")

