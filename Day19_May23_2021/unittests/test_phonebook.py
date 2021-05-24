import unittest

from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):


# Needs a setup method, thats one of the methods that I inherit from the test case super class.
# So now we will construct a fresh instance of phonebook, before each test-case executes.

    def setUp(self) -> None:
        self.phonebook = PhoneBook()

# setUp is called before every test method and tearDown is called afterwards.
    def tearDown(self) -> None:
        pass

    def test_lookup_by_name(self):
    #        phonebook = PhoneBook()
            self.phonebook.add("Bharath", "123456")
            number =  self.phonebook.lookup("Bharath")
            self.assertEqual("123456", number)

# I want to check what happens, When I look up a name i.e. not present in my phonebook...may raise a key error.

    def test_missing_name(self):
#        phonebook = PhoneBook()
        # We need to put the KeyError in Context manager
        # This means the unittest will ensure that the lines enclosed with the "With" statement will throw a key error, and if they do then the test will pass.
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

# Another test cases like, 1.If the two persons have same phone number or one is prefix of the other.

# 3. The simplest case is with an empty phonebook, which of course should be consistent. Lets write a new test case for that.
#    @unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
#            phonebook = PhoneBook()
        self.assertTrue(self.phonebook.is_consistent())

# Example of poor test-case design
# We have not executed the last two lines of the test case, and thats the way unit testing framework works.
# As soon as an exception is encountered, it breaks off and doesn't execute the rest of the test case, so just from the test results,
# we don't know what functionality is not working or could be working after the failing assertion.
# Of course there are other unit testing frameworks that might not have this behaviour that it halts execution at the first exception.

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Anna", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_entries(self):
        self.phonebook.add("Bob", "12345") #identical to Bob
        self.phonebook.add("Sue", "12345")  # identical to Bob
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_prefix(self):
        self.phonebook.add("Bob", "12345") #Prefix to Bob
        self.phonebook.add("Sue", "123")
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add("Sue", "123343")
        self.assertIn("Sue", self.phonebook.get_names())
        self.assertIn("123343", self.phonebook.get_numbers())