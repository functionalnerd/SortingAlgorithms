"""
Custom implementation of selection sort algorithm.

Selection sort is an in-place comparison sorting algorithm, O(n^2). The
algorithm divides the input list into two parts: the sublist of items already
sorted, which is built up from left to right at the front (left) of the list,
and the sublist of items remaining to be sorted that occupy the rest of the
list. Initially, the sorted sublist is empty and the unsorted sublist is the
entire input list. The algorithm proceeds by finding the smallest (or largest,
depending on sorting order) element in the unsorted sublist, exchanging
(swapping) it with the leftmost unsorted element (putting it in sorted order),
and moving the sublist boundaries one element to the right.
"""
import __builtin__

__author__ = "Justin Oliver"
__email__ = "functionaln3rd@gmail.com"

def sort(aggr, cmp=None, key=None, reverse=False):
    """
    Sorts the aggregate.

    Using selection sort, the data is sorted in O(n^2). The data aggregate is
    assumed to be iterable. If a key is passed, it is called on each element.
    Finally, if a cmp is passed, it will be used when comparing two elements.

    :param obj data: aggregate to be sorted
    :param func cmp: function used to compare two elements
    :param func key: function called on each element before it is compared
    :returns: sorted data
    """
    aggr = list(aggr)

    for i, element in enumerate(aggr):
        # Get the next element to swap with
        swap_index = i
        for j in xrange(i+1, len(aggr)):
            # Get the data to be compared
            if key:
                data = key(aggr[j])
                swap_data = key(aggr[swap_index])
            else:
                data = aggr[j]
                swap_data = aggr[swap_index]

            # Get the result of the compare
            if cmp and reverse is False:
                result = cmp(data, swap_data)
            elif cmp and reverse is True:
                result = cmp(swap_data, data)
            if reverse is False:
                result = __builtin__.cmp(data, swap_data)
            else:
                result = __builtin__.cmp(swap_data, data)

            if result < 0:
                swap_index = j

        # Swap if necessary
        if swap_index != i:
            aggr[i] = aggr[swap_index]
            aggr[swap_index] = element

    return aggr
