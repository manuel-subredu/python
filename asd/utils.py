def __is_array_sorted__(v, start, end):
    pass


def is_array_sorted(v):
    if len(v) == 0:
        return False

    if len(v) == 1:
        return v[0] < v[1]

    for i in range(1, len(v) - 1):
        if v[i] > v[i+1]:
            return False

    return True
