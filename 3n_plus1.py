prev = {}


def collatz(n, i):
    if n % 2 == 0:
        return n/2, i+1
    return (3*n+1)/2, i+2


def hailstone_length(n):
    og_n = n
    i = 0
    while n != 1:
        if n in prev:
            ans = i + prev[n]
            prev[og_n] = ans
            return ans + 1
        n, i = collatz(n, i)
    prev[og_n] = i
    return i + 1


def largest_hailstone(start, end):
    return max(map(hailstone_length, range(start, end+1)))


if __name__ == '__main__':
    import sys
    try:
        start = sys.stdin.readline()
        end = sys.stdin.readline()
        start, end = int(start), int(end)
    except TypeError as e:
        print(e)
        sys.exit()
    print(largest_hailstone(start, end))
