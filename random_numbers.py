import random

my_list = list("abcdefghigklmnopqrstuvwxyz")
a = random.sample(my_list, 4)

for i in range(10):
    print(random.sample(my_list, 5))
