

"""
Ref: https://www.geeksforgeeks.org/binary-search/?ref=lbp

Complexity: O(log n base 2)
"""
def __binary_search__(v, k, start, end):
    if start < 0:
        raise RuntimeError('start cannot be smaller than 0')
    if end >= len(v):
        raise RuntimeError(f'end({end}) is greater than the number of elements in array: {len(v)}')
    if start > end:
        raise RuntimeError(f'start index ({start})cannot be greater than end index ({end})')

    if start > end or end < start:
        return False

    idx = start + round ((end - start) / 2)
    if v[idx] == k:
        return idx

    if v[idx] > k:
        return __binary_search__(v, k, start, idx - 1)
    else:
        return __binary_search__(v, k, idx + 1, end)

"""
Wrapper for actual binary search. In this function we make some edge cases checks
"""
def binary_search(v, k):
    if v is None or len(v) == 0:
        raise RuntimeError('Invalid array: not defined or empty')
    if k is None:
        raise RuntimeError('Item to search is not valid')

    return __binary_search__(v, k, 0, len(v)-1)