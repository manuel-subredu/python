

def binary_search(v, k, start, end):
    if v is None or len(v) == 0:
        raise RuntimeError('Invalid array: not defined or empty')
    if k is None:
        raise RuntimeError('Item to search is not valid')
    if start < 0:
        raise RuntimeError('start cannot be smaller than 0')
    if end >= len(v):
        raise RuntimeError(f'end({end}) is greater than the number of elements in array: {len(v)}')
    if start >= end:
        raise RuntimeError(f'start index ({start})cannot be greater than end index ({end})')

    if start > end or end < start:
        return False

    idx = start + round ((end - start) / 2)
    if v[idx] == k:
        return idx

    if v[idx] > k:
        return binary_search(v, k, start, idx - 1)
    else:
        return binary_search(v, k, idx + 1, end)