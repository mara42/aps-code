def pancakesort(arr):
    flips = []
    if len(arr) <= 1:
        return arr
    for i in range(len(arr), 1, -1):
        max_i = max(range(i), key=arr.__getitem__)
        # print('max_i=', max_i)
        if max_i+1 != i:
            # This indexed max needs moving
            if max_i != 0:
                # Flip the max item to the left
                arr[:max_i+1] = reversed(arr[:max_i+1])
                print(arr)
                flips.append(max_i + 1)
            # Flip it into its final position
            arr[:i] = reversed(arr[:i])
            flips.append(i + 1)
    print(flips)


if __name__ == '__main__':
    tutor = True
    # data = [int(e) for e in "46 33 10 35 36 11 29 16 17 31 30 40 32 27 18 41 34 15 43 23 20 25 22 12 19 24 21 44 39 26 38 42 37 45 28 13 9".split(' ')]
    data = [int(e) for e in "11 13 18 19 20 41 50 38 6 42 7 24 3 26 33 31 28".split()] # 9 10 45 47 30 39 21 4 27 44 22 2 8 5 29 48 23 16 36 34 49 25 12 17 37 35 43 15 46 14 32".split(' ')]
    print('Original List: %r' % ' '.join(str(e) for e in data))
    pancakesort(data)
    print('Pancake Sorted List: %r' % ' '.join(str(e) for e in data))
