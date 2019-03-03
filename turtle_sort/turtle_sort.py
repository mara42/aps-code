def count_turtle_sort_steps(not_sorted, is_sorted, turtle_count):
    # find how many turtles don't need to be moved, return the difference
    expected_turtle = actual_turtle = turtle_count - 1
    need_to_move = 0
    while actual_turtle >= 0:
        if is_sorted[expected_turtle] == not_sorted[actual_turtle]:
            expected_turtle, actual_turtle = expected_turtle-1, actual_turtle-1
        else:
            actual_turtle = actual_turtle-1
            need_to_move += 1
    return need_to_move


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
