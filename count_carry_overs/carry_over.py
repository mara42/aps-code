#!/usr/bin/env python3
from itertools import zip_longest


def first_try_carry_over(a, b):
    total_carries = 0
    carry_over = 0
    for a_i, b_i in zip_longest(a, b, fillvalue=0):
        if carry_over + a_i + b_i >= 10:
            total_carries += 1
            carry_over = 1
        else:
            carry_over = 0
    return total_carries


if __name__ == '__main__':
    import sys
    tuples = []
    for line in sys.stdin:
        if line == "0 0\n":
            break
        else:
            tupl = line.rstrip().split(' ')
        tuples.append(tupl)
    for a, b in tuples:
        try:
            b = [int(y) for y in reversed(b)]  # iterators rock
            a = [int(x) for x in reversed(a)]
        except TypeError as e:
            print(e)
            sys.exit()
        carries = first_try_carry_over(a, b)
        if carries == 0:
            carries = 'No'
        print('{} carry operations.'.format(carries))
