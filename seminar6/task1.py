# бинарный поиск
def binsearch(array, value):
    min_index = 0
    max_index = len(array) - 1
    while (max_index >= min_index) and (array[max_index] >= value >= array[min_index]):
        index = (min_index + max_index) // 2
        if array[index] == value:
            return index
        elif array[index] > value:
            max_index = index - 1
        else:
            min_index = index + 1
    return -1 # Если искали в массиве, но не нашли

array = [1, 2, 3, 5, 7, 11, 13]

print(binsearch(array, 0))

print(binsearch(array, 14))

print(binsearch(array, 6))

print(binsearch(array, 1))

print(binsearch(array, 7))
