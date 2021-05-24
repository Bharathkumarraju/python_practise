bharathdasaraju@MacBook-Pro phonebook_pytest $ python3 -m pytest
===================================================================================================================== test session starts ======================================================================================================================
platform darwin -- Python 3.7.4, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/bharathdasaraju/PycharmProjects/phonebook_pytest
collected 1 item

test_phonebook.py F                                                                                                                                                                                                                                      [100%]

=========================================================================================================================== FAILURES ===========================================================================================================================
_____________________________________________________________________________________________________________________ test_lookup_by_name ______________________________________________________________________________________________________________________

    def test_lookup_by_name():
>       phonebook = Phonebook()
E       NameError: name 'Phonebook' is not defined

test_phonebook.py:2: NameError
=================================================================================================================== short test summary info ====================================================================================================================
FAILED test_phonebook.py::test_lookup_by_name - NameError: name 'Phonebook' is not defined
====================================================================================================================== 1 failed in 0.09s =======================================================================================================================
bharathdasaraju@MacBook-Pro phonebook_pytest $






bharathdasaraju@MacBook-Pro phonebook_pytest $ python3 -m pytest
========================================================================================= test session starts ==========================================================================================
platform darwin -- Python 3.7.4, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/bharathdasaraju/PycharmProjects/phonebook_pytest
collected 1 item

test_phonebook.py F                                                                                                                                                                              [100%]

=============================================================================================== FAILURES ===============================================================================================
_________________________________________________________________________________________ test_lookup_by_name __________________________________________________________________________________________

    def test_lookup_by_name():
        phonebook = Phonebook()
        phonebook.add("Bob", "1234")
>       assert "1234" == phonebook.lookup("Bob")
E       AssertionError: assert '1234' == None
E        +  where None = <bound method Phonebook.lookup of <test_phonebook.Phonebook object at 0x10afc6450>>('Bob')
E        +    where <bound method Phonebook.lookup of <test_phonebook.Phonebook object at 0x10afc6450>> = <test_phonebook.Phonebook object at 0x10afc6450>.lookup

test_phonebook.py:12: AssertionError
======================================================================================= short test summary info ========================================================================================
FAILED test_phonebook.py::test_lookup_by_name - AssertionError: assert '1234' == None
========================================================================================== 1 failed in 0.12s ===========================================================================================
bharathdasaraju@MacBook-Pro phonebook_pytest $





Testing started at 13:44 ...
/usr/local/bin/python3.7 "/Applications/PyCharm CE.app/Contents/helpers/pycharm/_jb_pytest_runner.py" --path /Users/bharathdasaraju/PycharmProjects/phonebook_pytest/test_phonebook.py
Launching pytest with arguments /Users/bharathdasaraju/PycharmProjects/phonebook_pytest/test_phonebook.py in /Users/bharathdasaraju/PycharmProjects/phonebook_pytest

============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/local/opt/python/bin/python3.7
cachedir: .pytest_cache
rootdir: /Users/bharathdasaraju/PycharmProjects/phonebook_pytest
collecting ... collected 1 item

test_phonebook.py::test_lookup_by_name PASSED                            [100%]

============================== 1 passed in 0.01s ===============================

Process finished with exit code 0


