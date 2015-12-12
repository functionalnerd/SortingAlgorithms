"""
Module responsible for testing sorting algorithms.
"""
from random import shuffle
from numpy import random as nprnd
from selection_sort import sort as sel_sort

__author__ = "Justin Oliver"
__email__ = "functionaln3rd@gmail.com"

def lists_equal(list1, list2, key=None):
    """
    Compares if two lists are equal and assumes the lists are valid with the
    same length.
    """
    if key is None:
        return list1 == list2

    for i in xrange(len(list1)):
        if key(list1[i]) != key(list2[i]):
            return False

    return True


def test(sort):
    """
    Tests sorting algorithm with the passed data.
    """
    print "Testing sort functionality for {}...".format(sort.__name__)

    # Shuffle the data, testing various ways to sort
    data = nprnd.randint(-1000, 1000, size=1000)
    assert sorted(data) == sort(data)

    shuffle(data)
    assert sorted(data, reverse=True) == sort(data, reverse=True)

    shuffle(data)
    assert lists_equal(sorted(data, key=abs), sort(data, key=abs), key=abs)

    print "Test succeeded!"


if __name__ == "__main__":
    test(sel_sort)
