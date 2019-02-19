def findStart(A, k, l, h):
    # find left most occurance of k in array A
    if h < l:
        return l
    m = (l+h) // 2
    if A[m] < k:
        return findStart(A, k, m+1, h)
    else:
        return findStart(A, k, l, m-1)


def findEnd(A, k, l, h):
    # find the index of the last occurance of k in the array
    if l > h:
        return l
    m = (l+h) // 2
    if A[m] > k:
        return findEnd(A, k, l, m-1)
    else:
        return findEnd(A, k, m+1, h)


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 5, 5, 5, 5, 6, 7]
    a = findStart(arr, 5, 0, len(arr))
    b = findEnd(arr, 5, 0, len(arr))
    print(b-a)
    print(a, b)
    print(arr[4:8])

