#  Unpacking

# *_ will ignore the value of the variable
a, b, *_, c, d = (1, 2, 3, 4, 5, 6)
print(a, b, c, d)  # 1 2 5 6
