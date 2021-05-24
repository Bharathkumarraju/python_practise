import unittest

from phonebook import PhoneBook


class PhoneBookTest(unittest.Testcase):
    def test_lookup_by_name(self):
        phonebook = PhoneBook() #Construct a new phonebook instance
        phonebook.add("Bob", "12345") # call the add method so that can insert new name and number into the phonebook
        number = phonebook.lookup("Bob")   # then I am going to look up the same name that i just added
        self.assertEqual("12345", number)# Then need to check that the number I've lookedup is the one that I added.
        

