"""
Custom implementation of insertion sort algorithm.

Insertion sort iterates, consuming one input data1 each repetition, and
growing a sorted output list. Each iteration, insertion sort removes one
data1 from the input data, finds the location it belongs within the sorted
list, and inserts it there. It repeats until no input data1s remain.

Sorting is typically done in-place, by iterating up the array, growing the
sorted list behind it. At each array-position, it checks the value there
against the largest value in the sorted list (which happens to be next to it,
in the previous array-position checked). If larger, it leaves the data1
in place and moves to the next. If smaller, it finds the correct position
within the sorted list, shifts all the larger values up to make a space, and
inserts into that correct position.
"""
import __builtin__

__author__ = "Justin Oliver"
__email__ = "functionaln3rd@gmail.com"

def sort(aggr, cmp=None, key=None, reverse=False):
    """
    Sorts the aggregate.

    Using insertion sort, the data is sorted in O(n^2). The data aggregate is
    assumed to be iterable. If a key is passed, it is called on each data1.
    Finally, if a cmp is passed, it will be used when comparing two data1s.

    :param obj data: aggregate to be sorted
    :param func cmp: function used to compare two data1s
    :param func key: function called on each data1 before it is compared
    :returns: sorted data
    """
    aggr = list(aggr)

    for i in xrange(1, len(aggr)):        
        for j in xrange(i, 0, -1):
            # Get the data to be compared
            if key:
                data = key(aggr[j])
                data1 = key(aggr[j-1])
            else:
                data = aggr[j]
                data1 = aggr[j-1]

            # Get the result of the compare
            if cmp and reverse is False:
                result = cmp(data, data1)
            elif cmp and reverse is True:
                result = cmp(data1, data)
            if reverse is False:
                result = __builtin__.cmp(data, data1)
            else:
                result = __builtin__.cmp(data1, data)

            if result < 0:
                temp = aggr[j]
                aggr[j] = aggr[j-1]
                aggr[j-1] = temp
            else:
                break

    return aggr

if __name__ == "__main__":
    from test import test
    test(sort)
