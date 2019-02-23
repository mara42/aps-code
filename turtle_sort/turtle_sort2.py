def count_turtle_sort_steps(not_sorted, is_sorted, length):
    i = j = length - 1
    shifted = 0
    while j >= 0:
        if is_sorted[i] == not_sorted[j]:
            i, j = i-1, j-1
        else:
            shifted += 1
            j = j-1
    return shifted


if __name__ == '__main__':
    asdf = """2
3
Yertle
Duke of Earl
Sir Lancelot
Duke of Earl
Yertle
Sir Lancelot
9
Yertle
Duke of Earl
Sir Lancelot
Elizabeth Windsor
Michael Eisner
Richard M. Nixon
Mr. Rogers
Ford perfect
Mack
Yertle
Richard M. Nixon
Sir Lancelot
Duke of Earl
Elizabeth Windsor
Michael Eisner
Mr. Rogers
Ford perfect
Mack"""
    import sys
    arrays = []
    try:
        # for line in [e for e in asdf.split('\n') if e]:
        for line in sys.stdin:
            arrays.append(line.strip())
    except TypeError as e:
        print(e)
        sys.exit()
    tests = int(arrays.pop(0))
    for _ in range(tests):
        unsorted_case = []
        sorted_case = []
        amount = int(arrays.pop(0))
        for __ in range(amount):
            unsorted_case.append(arrays.pop(0))
        for __ in range(amount):
            sorted_case.append(arrays.pop(0))
        print(count_turtle_sort_steps(unsorted_case, sorted_case, amount))

# a = """
# Yertle
# Duke of Earl
# Sir Lancelot
# Elizabeth Windsor
# Michael Eisner
# Richard M. Nixon
# Mr. Rogers
# Ford perfect
# Mack
# """
# b = """
# Yertle
# Richard M. Nixon
# Sir Lancelot
# Duke of Earl
# Elizabeth Windsor
# Michael Eisner
# Mr. Rogers
# Ford perfect
# Mack
# """

# a = [e for e in a.split('\n') if e]
# b = [e for e in b.split('\n') if e]
# # e = [2, 1, 4, 5, 3]
# # e = [2, 1, 5, 4, 3]
# e = [6, 8, 2, 1, 3, 9, 7, 5, 4]
# # e = [1, 2, 3, 5, 4]
# # e = ['Yertle',
# #       'Duke of Earl',
# #       'Sir Lancelot',
# #       'Elizabeth Windsor',
# #       'Michael Eisner',
# #       'Richard M. Nixon',
# #       'Mr. Rogers',
# #       'Ford perfect',
# #       'Mack']

# print(count_turtle_sort_steps(a, b, len(a)))
# print(count_turtle_sort_steps(e, sorted(e), len(e)))
