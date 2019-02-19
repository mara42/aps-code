tutor = False


def pancakesort(data):
    flips = []
    if len(data) <= 1:
        return data
    for size in range(len(data), 1, -1):
        maxindex = max(range(size), key=data.__getitem__)
        if maxindex+1 != size:
            # This indexed max needs moving
            if maxindex != 0:
                # Flip the max item to the left
                data[:maxindex+1] = reversed(data[:maxindex+1])
                flips.append(maxindex + 1)
            # Flip it into its final position
            data[:size] = reversed(data[:size])
            flips.append(size + 1)
    printl(flips)

if __name__ == '__main__':
    tutor = True
    # data = [int(e) for e in "46 33 10 35 36 11 29 16 17 31 30 40 32 27 18 41 34 15 43 23 20 25 22 12 19 24 21 44 39 26 38 42 37 45 28 13 9".split(' ')]
    data = [int(e) for e in "11 13 18 19 20 41 50 38 6 42 7 24 3 26 33 31 28 9 10 45 47 30 39 21 4 27 44 22 2 8 5 29 48 23 16 36 34 49 25 12 17 37 35 43 15 46 14 32".split(' ')]
    data = [int(e) for e in "67 54 58 6 12 71 86 88 27 22 35 43 9 25 93 59 28 10 72 42 74 61 84 41 3 89 19 45 16 65 7 85 51 53 66 79 90 97 40 29 14 77 78 38 15 5 39 62 82 48 92 17 49 73 68 70 24 30 8 91 52 36 34 64 63 23 46 69 31 37 95 83 50 76 32 81 18 11 80 20 26 94 60 56 4 21 47 33 44 75 87 13 96 55".split(' ')]
    print('Original List: %r' % ' '.join(str(e) for e in data))
    pancakesort(data)
    print('Pancake Sorted List: %r' % ' '.join(str(e) for e in data))
