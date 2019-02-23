def count_turtle_sort_steps(not_sorted, is_sorted, length):
    i = j = length - 1
    shifted = 0
    while j >= 0:
        if is_sorted[i] == not_sorted[j]:
            i, j = i-1, j-1
        else:
            shifted += 1
            j = j-1
    return shifted


if __name__ == '__main__':
    import sys
    arrays = []
    try:
        for line in sys.stdin:
            arrays.append(line.strip())
    except TypeError as e:
        print(e)
        sys.exit()
    tests = int(arrays.pop(0))
    for _ in range(tests):
        unsorted_case = []
        sorted_case = []
        amount = int(arrays.pop(0))
        for __ in range(amount):
            unsorted_case.append(arrays.pop(0))
        for __ in range(amount):
            sorted_case.append(arrays.pop(0))
        print(count_turtle_sort_steps(unsorted_case, sorted_case, amount))
