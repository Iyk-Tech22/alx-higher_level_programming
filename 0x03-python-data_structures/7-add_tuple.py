#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_1 = list(tuple_a)
    tuple_2 = list(tuple_b)
    tuples = []
    for i in range(0, 2):
        if len(tuple_1) < 2:
            tuple_1.append(0)
        if len(tuple_2) < 2:
            tuple_2.append(0)
        tuples.append(tuple_1[i] + tuple_2[i])
    return (tuple(tuples))
