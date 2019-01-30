def square(n):
    increment = 1
    res = 0
    for i in range(1, n+1):
        res += increment
        increment += 2
    return res


print(0)

# invariant i >= i, increment is odd, n = i*i
# square = i * increment + 1

# \sigma^n_i=1 i + 2

# invariant? square_n = square_n-1 + n * 2 - 1, for all natural numbers greater than 0
