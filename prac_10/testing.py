"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=6):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    test_car = Car(fuel=10)
    assert test_car.fuel == 10

    test_car = Car(fuel=100)
    assert test_car.fuel == 100


run_tests()


# (PyCharm may see your >>> doctest comments and run doctests anyway.)
# doctest.testmod()


def create_sentence_from_phrases(phrases):
    """
    pass
    >>> create_sentence_from_phrases('hello.')
    'Hello.'
    >>> create_sentence_from_phrases('it is an ex parrot.')
    'It is an ex parrot.'
    >>> create_sentence_from_phrases('this is my sentence.')
    'This is my sentence.'
    """

    sentence = phrases.capitalize()
    return sentence


doctest.testmod()
