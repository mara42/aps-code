def shortestSumDistance(houses):
    sorted_houses = sorted(houses)  # ideally would be be QuickSelect
    median = sorted_houses[len(sorted_houses) // 2]
    return sum(map(lambda a: abs(median - a), sorted_houses))


if __name__ == '__main__':
    import sys
    tests = []
    try:
        for line in sys.stdin:
            # discarding number of houses, not necessary for list
            tests.append([int(e) for e in line.split(' ')[1:] if e])
    except TypeError as e:
        print(e)
        sys.exit()
    del tests[0]  # get rid of number of tests as stdin, does not care
    for test in tests:
        print(shortestSumDistance(test))

"""
expected output
2
4
12693
"""
