def digitSum(n):
    su = 0
    while n > 0:
        su += n % 2
        n //= 2
    return su


def count_carry_overs(a, b):
    return (digitSum(a) + digitSum(b) - digitSum(a + b))


print(count_carry_overs(2, 7))
