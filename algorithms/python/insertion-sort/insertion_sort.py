'''
Reference:
    Introduction to Algorihths, CLRS

Notes:
    Expository notes on the Insertion Sort algorithm, a sorting method
    I've never looked at.
'''

def sort(arr):
    '''Given an unsorted array, sort it.'''
    for i, elem in enumerate(arr):
        # a single element is sorted (trivially)
        if i == 0: continue

        # for each iteration, everything up to i is in order.
        # we need only find the correct spot for arr[i] (elem)
        # in the subarray [0..arr[i - 1]]

        # start in the position just before i when looking for the
        # correct insertion index, and work backwards
        insertion_index = i - 1

        while insertion_index >= 0 and arr[insertion_index] > elem:
            # iterate backwards until we find an index where the current
            # element is greater, or if it is smaller than all elements,
            # we insert it at i = 0.
            arr[insertion_index + 1] = arr[insertion_index]
            insertion_index -= 1

        # insert the element
        arr[insertion_index + 1] = elem

'''
# Analysis

_Loop Invariant:_
    At the start of each iteration of the for loop (lines 12:29),
    the subarry arr[0..i-1] consists of the elements originally in
    arr[0..i-1], but in sorted order.
'''
