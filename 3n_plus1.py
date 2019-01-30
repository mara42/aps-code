prev = {}


def collatz(n, i):
    if n % 2 == 0:
        return n/2, i+1
    return (3*n+1)/2, i+2


def thing(n):
    og_n = n
    i = 0
    while n != 1:
        if n in prev:
            ans = i + prev[n]
            # prev[og_n] = ans
            return ans + 1
        n, i = collatz(n, i)
    prev[og_n] = i
    return i + 1


def brute(n):
    i = 1
    while n != 1:
        n, i = collatz(n, i)
    return i


def things_between(start, end):
    return max(map(thing, range(start, end+1)))


# print(thing(11000000))
# print(thing(22))
# print(thing(100))
# print(thing(2))

# print(brute(22))
# print(brute(100))
print(things_between(16, 100))  # 119
# print(things_between(1, 1000000))  # 1, 1000000 = 525
for i in prev.items():
    print(i)
