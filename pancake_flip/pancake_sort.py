def pancake_sort(arr):
    arr_len = len(arr) - 1
    flips = []
    i = 0
    for i in range(arr_len+1):
        max_i = arr.index(max(arr[i:]))
        if max_i != i:
            if max_i != arr_len:
                flips.append(max_i + 1)
                arr[max_i:] = reversed(arr[max_i:])
            flips.append(i + 1)
            arr[i:] = reversed(arr[i:])
    flips.append(0)
    print(arr)
    return flips


if __name__ == '__main__':
    import sys
    arrays = []
    try:
        for line in sys.stdin:
            arrays.append([int(e) for e in line.split(' ') if e])
    except TypeError as e:
        print(e)
        sys.exit()
    del arrays[-1]  # remove the pesky 0 at the end
    for array in arrays:
        print(' '.join((str(e) for e in array)))
        print(' '.join((str(n) for n in pancake_sort(array))))
    print(0)
