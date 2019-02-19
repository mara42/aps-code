def pancake_sort(arr):
    arr_len = len(arr) - 1
    flips = []
    i = 0
    for i in range(arr_len+1):
        # TODO: if largest element in position, do nothing,
        # if not in last or first position move to first,
        #  if if in first position move to final position
        max_i = arr.index(max(arr[i:]))
        if max_i != i:
            if max_i != arr_len:
                flips.append(max_i + 1)
                arr[max_i:] = reversed(arr[max_i:])
            flips.append(i + 1)
            arr[i:] = reversed(arr[i:])

        # if i == max_i:
        #     i += 1
        # elif max_i == arr_len-1:
        #     flips.append(i + 1)
        #     arr[i:] = reversed(arr[i:])
        # else:
        #     flips.append(max_i + 1)
        #     arr[max_i:] = reversed(arr[max_i:])
    flips.append(0)
    print(arr)
    return flips


if __name__ == '__main__':
    # goal is 5,4,3,2,1
    import sys
    arrays = []
    try:
        # for line in sys.stdin:
            # arrays.append([int(e) for e in line.split(' ') if e])
            pass
    except TypeError as e:
        print(e)
        sys.exit()
    if len(arrays) == 0:
        # arrays = [[9, 2, 3, 88, 5, 1, 10, 4, 233], [23, 1, 33, 45, 2], [0]]
        # arrays = [[2]]
        arrays.append([int(e) for e in "11 13 18 19 20 41 50 38".split(' ')]) # 6 42 7 24 3 26 33 31 28 9 10 45 47 30 39 21 4 27 44 22 2 8 5 29 48 23 16 36 34 49 25 12 17 37 35 43 15 46 14 32".split(' ')])
        arrays.append([0])
    del arrays[-1]  # remove the pesky 0 at the end
    for array in arrays:
        print(' '.join((str(e) for e in array)))
        print(' '.join((str(n) for n in pancake_sort(array))))
        # print(pancake_sort(array))
        # bg_max = (5 * len(array) + 5) / 3
        # print(bg_max,  ' vs ', len(pancake_sort(array)))
    print(0)
