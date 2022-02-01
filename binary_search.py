import time


def binary_search(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start+end) // 2
        if target == arr[mid]:
            return mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = start + 1
    return -1


x = [i for i in range(1, 1000)]


start = time.time()
print(binary_search(x, 23))
end = time.time()
print(end - start)
