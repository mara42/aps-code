def pancake_sort(arr):
    arr_len = len(arr)
    flips = []
    i = 0
    while arr_len - i > 0:
        max_i = arr.index(max(arr[i:]))
        if i == max_i:
            i += 1
        elif max_i == arr_len-1:
            flips.append(i + 1)
            arr[i:] = reversed(arr[i:])
        else:
            flips.append(max_i + 1)
            arr[max_i:] = reversed(arr[max_i:])
    flips.append(0)
    return flips


def selection_sort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]


if __name__ == '__main__':
    import sys
    arrays = []
    try:
        for line in sys.stdin:
            arrays.append([int(e) for e in line.split(' ') if e])
    except TypeError as e:
        print(e)
        sys.exit()
    del arrays[-1]
    for array in arrays:
        print(' '.join([str(e) for e in array]))
        print(' '.join([str(n) for n in pancake_sort(array)]))
    print(0)
