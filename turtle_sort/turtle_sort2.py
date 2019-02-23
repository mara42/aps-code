def count_turtle_sort_steps(not_sorted, is_sorted, length):
    i = j = length - 1
    shifted = []
    while j >= 0:
        if is_sorted[i] == not_sorted[j]:
            i, j = i-1, j-1
        else:
            shifted.append(not_sorted[j])
            j = j-1
    b = max(shifted, key=lambda a: is_sorted.index(a))
    return is_sorted.index(b) + 1


a = """
Yertle
Duke of Earl
Sir Lancelot
Elizabeth Windsor
Michael Eisner
Richard M. Nixon
Mr. Rogers
Ford perfect
Mack
"""
b = """
Yertle
Richard M. Nixon
Sir Lancelot
Duke of Earl
Elizabeth Windsor
Michael Eisner
Mr. Rogers
Ford perfect
Mack
"""

a = [e for e in a.split('\n') if e]
b = [e for e in b.split('\n') if e]
# e = [2, 1, 4, 5, 3]
# e = [2, 1, 5, 4, 3]
e = [6, 8, 2, 1, 3, 9, 7, 5, 4]
# e = [1, 2, 3, 5, 4]
# e = ['Yertle',
#       'Duke of Earl',
#       'Sir Lancelot',
#       'Elizabeth Windsor',
#       'Michael Eisner',
#       'Richard M. Nixon',
#       'Mr. Rogers',
#       'Ford perfect',
#       'Mack']

# print(count_turtle_sort_steps(a, b, len(a)))
print(count_turtle_sort_steps(e, sorted(e), len(e)))
