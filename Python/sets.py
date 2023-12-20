set = {1, 2, 34, 5, 5, 6, 6, 7, 78678, 87, 78, 7}

print(set)

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [1, 2, 3, 4, 5, 63355, 7, 8, 9, 10]
obj = {"test": "aaaaa", "test2": "Linn", "test3": "Sam"}
# spread obj values

arr3 = {*arr1, *arr2, *obj.values()}
print("arrr3", arr3)
