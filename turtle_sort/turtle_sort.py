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
cur = 'nixon',

# simple_way = enumerate(b), find largest element that is too shallow
# can be done O(n), go through array[::-1], check if same element in both indexes,
# if not same element, take note of wrong element in unsorted array, don't increment
# index of sorted array, keep checking this way
# 1. check if equal, if so then move both indexes forwards
# 2. if not equal, note down unsorted array value, only increment unsorted array
# 3. repeat 1 and 2 until you find the largest element not in place, replacing the noted value if

# TODO: make naïve version
# enumerate sorted list, iterate through lists, make note of elements not in place, when something is not in place pause iteration on sorted array, choose largest element in the array of out of place elements, number of steps to sort using turtlesort will be the largest outplace index value -1
# out of place is about being too shallow

# how to do: [2, 1, 3, 4, 5, 0] ??? i.e. count swaps in constant time

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

b1 = list(enumerate(b, 1))

"""
a1 = [1, 4, 3, 5, 6, 2, 7, 8, 9]
# find first number that is missing
# move 3
a2 = [3, 1, 4, 5, 6, 2, 7, 8, 9]
# move 2
a3 = [2, 3, 1, 4, 5, 6, 7, 8, 9]
# move 1
a3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

how to choose 3 intially? It's already in place
- first element after an element that is too high? i.e. 3 cuz it's after 4
 and 4 is too high
- find first too shallow element, move all element smaller than it up in
decending order
- find largest element out of place, bubble up all element smaller than it.
- number of moves is largest index out of place - 1
"""
a1 = [1, 4, 3, 9, 5, 6, 2, 7, 8]
a2 = []

"""
below is the using a sorting method of finding elements not in place that are
too small for their position, moving those up.
a1 = [1, 4, 3, 5, 6, 2, 7, 8, 9]
# move candidates: 2, 4
a2 = [2, 1, 4, 3, 5, 6, 7, 8, 9]
# move candidates: 3, 1
a3 = [3, 2, 1, 4, 5, 6, 7, 8, 9]
# move candidates: 1
a3 = [1, 3, 2, 4, 5, 6, 7, 8, 9]
# move candidates: 2
a3 = [2, 1, 3, 4, 5, 6, 7, 8, 9]
# move candidates: 1
a3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

moves: 5, goal: 3
Not efficient enough
"""

print(b1)
