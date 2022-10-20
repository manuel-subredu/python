import array


def gen_fibonacci(steps = 100):
    v = array.array('d')
    a, b = 0, 1

    for i in range(steps):
        v.append(a+b)
        a, b = b, a+b

    return v


def gen_vector_even(steps=100):
    v = array.array('I')

    for i in range(steps):
        v.append(i*2)

    return v


def gen_vector_odd(steps=100):
    v = array.array('I')

    for i in range(steps):
        v.append(i*2 + 1)

    return v