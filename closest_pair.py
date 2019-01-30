from itertools import product
from math import sqrt

points = ((0, 0), (1, 1), (4, 1), (5, 1), (8, 8))


def dist(a, b):
    return sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)


def connect(point1, point2, series):
    series.append((point1, point2))


def closest_pair(p):
    chain = []
    # end_point1 = None
    # end_point2 = None
    n = len(p)
    for _ in range(1, n-1):
        d = float('inf')
        for s, t in product(points, repeat=2):
            distance = dist(s, t)
            if distance <= d:
                s_max, t_max = s, t
                d = distance
        connect(s_max, t_max, chain)
    return chain


print(closest_pair(points))
