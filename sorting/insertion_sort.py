"""
Custom implementation of insertion sort algorithm.

Insertion sort iterates, consuming one input element each repetition, and 
growing a sorted output list. Each iteration, insertion sort removes one 
element from the input data, finds the location it belongs within the sorted 
list, and inserts it there. It repeats until no input elements remain.

Sorting is typically done in-place, by iterating up the array, growing the 
sorted list behind it. At each array-position, it checks the value there 
against the largest value in the sorted list (which happens to be next to it, 
in the previous array-position checked). If larger, it leaves the element 
in place and moves to the next. If smaller, it finds the correct position 
within the sorted list, shifts all the larger values up to make a space, and 
inserts into that correct position.
"""
__author__ = "Justin Oliver"
__email__ = "functionaln3rd@gmail.com"

import __builtin__

def sort(aggr, cmp=None, key=None, reverse=False):
    """
    Sorts the aggregate.
    
    Using insertion sort, the data is sorted in O(n^2). The data aggregate is
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