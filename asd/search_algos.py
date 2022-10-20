

def binary_search(v, k, start, end):
    if start < 0:
        raise RuntimeError('start cannot be smaller than 0')
    if end >= len(v):
        raise RuntimeError(f'end({end}) is greater than the number of elements in array: {len(v)}')

    if start > end or end < start:
        return False

    idx = start + round ((end - start) / 2)
    if v[idx] == k:
        return idx

    if v[idx] > k:
        return binary_search(v, k, start, idx - 1)
    else:
        return binary_search(v, k, idx + 1, end)
