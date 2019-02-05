#!/usr/bin/env python3
from itertools import zip_longest


def first_try_carry_over(a, b):
    carry_over = 0
    temp = 0
    for x, y in zip_longest(a, b, fillvalue=0):
        if temp + x + y >= 10:
            carry_over += 1
            temp = 1
        else:
            temp = 0
    return carry_over


if __name__ == '__main__':
    import sys
    tuples = []
    for line in sys.stdin:
        line = line.rstrip()
        if line == "0 0":
            break
        else:
            tupl = line.split(' ')
        tuples.append(tupl)
    for a, b in tuples:
        try:
            b = [int(y) for y in reversed(b)]
            a = [int(x) for x in reversed(a)]
        except TypeError as e:
            print(e)
            sys.exit()
        res = first_try_carry_over(a, b)
        if res == 0:
            res = 'No'
        print(f'{res} carry operations.')
