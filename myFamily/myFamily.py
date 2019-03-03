def shortestSumDistance(houses):
    sorted_houses = sorted(houses)
    median = len(sorted_houses//2)
    return sum(map(lambda a: abs(sorted_houses[median]) - a), sorted_houses)


if __name__ == '__main__':
    import sys
    tests = []
    try:
        for line in sys.stdin:
            tests.append([int(e) for e in line.split(' ') if e])
    except TypeError as e:
        print(e)
        sys.exit()
    for test in tests:
        print(shortestSumDistance(test))

"""
expected output
2
4
12693
"""
