import array

"""Generate an array with steps elements that containts Fibonacci numbers. Numbers will be stored as doubles
"""
def gen_fibonacci(steps = 100):
    v = array.array('d')
    a, b = 0, 1

    for i in range(steps):
        v.append(a+b)
        a, b = b, a+b

    return v


"""Generate an array with steps elements that contains even numbers. Numbers are positive integers
"""
def gen_vector_even(steps=100):
    v = array.array('I')

    for i in range(steps):
        v.append(i*2)

    return v

"""Generate an array with steps elements that contains odd numbers. Numbers are positive integers
"""
def gen_vector_odd(steps=100):
    v = array.array('I')

    for i in range(steps):
        v.append(i*2 + 1)

    return v