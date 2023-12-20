from itertools import (
    product,
    permutations,
    combinations,
    combinations_with_replacement,
    accumulate,
    groupby,
)
import operator

# https://www.youtube.com/watch?v=3ecISAkioPc&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2&index=11
# Create a list of all possible combinations of the letters in the alphabet
a = [1, 2, 3]
b = [3, 4]
# prod = product(a, b) ->  [(1, 3), (1, 4), (2, 3), (2, 4)]
# options:
product(a, repeat=2)  # -> [(1, 3), (1, 4), (2, 3), (2, 4)]
# print(list(prod))

# permutation
#  return all possible ordering of an input list
perm = permutations(a)
# -> [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# print(list(perm))

# combinations
# return all possible combinations of a list
comb = combinations(a, 2)

# print(list(comb))  # ->  [(1, 2), (1, 3), (2, 3)]

# combinations_with_replacement
# return all possible combinations of a list with replacement
comb_wr = combinations_with_replacement(a, 2)
# print(list(comb_wr))  # -> [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

# accumulate
# return the accumulated sum of a list
# you can also use operator to change the operator to add, multiply, etc
a.append(4)
acc = accumulate(a)
# print(a)  # -> [1, 3, 6, 10, 15, 21]
# print(list(acc))  # -> [1, 3, 6, 10, 15, 21]
acc1 = accumulate(a, operator.mul)
print(list(acc1))  # -> [1, 3, 6, 10, 15, 21]


# groupby
# return a list of tuples where the first element is the key and the second element is the list of values
# groupby is useful for grouping data by a key
# gr = groupby(a, key=lambda x: x > 2)
# for key, value in gr:
#     # print(key, tuple(value))
#     pass


persons = [
    {"name": "John", "age": 20},
    {"name": "Bob", "age": 25},
    {"name": "Alice", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "Jack", "age": 20},
]

gr = groupby(persons, key=lambda x: x["age"])
for key, value in gr:
    print(key, list(value))
