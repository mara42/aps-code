def collatz(n, steps):
    if n % 2 == 0:
        return n//2, steps+1
    return (3*n+1)//2, steps+2


def hailstone_length(n):
    original_n = n-1
    step = 0
    while n != 1:
        if n < end and prev[n]:
            step += prev[n-1]
            break
        else:
            n, step = collatz(n, step)
    prev[original_n] = step
    return step + 1


def largest_hailstone(start, end):
    return max(map(hailstone_length, range(start, end+1)))


if __name__ == '__main__':
    import sys
    try:
        # start = sys.stdin.readline()
        # end = sys.stdin.readline()
        start, end = 1, 1e6
        start, end = int(start), int(end)
    except TypeError as e:
        print(e)
        sys.exit()
    prev = [0]*end
    print(largest_hailstone(start, end))
    print(len(prev))
