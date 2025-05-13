#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x_a = tuple_a + (0, 0)
    x_b = tuple_b + (0, 0)

    return (x_a[0] + x_b[0], x_a[1] + x_b[1])
