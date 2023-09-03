# сортировка слиянием
def merge_sort(array):
    if len(array) <= 1:
        return array
    max_index = len(array)
    middle_index = max_index // 2
    left_array = merge_sort(array[0 : middle_index])
    right_array = merge_sort(array[middle_index : max_index])
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            result.append(left_array[left_index])
            left_index += 1
        else:
            result.append(right_array[right_index])
            right_index += 1
    if left_index < len(left_array):
        for index in range(left_index, len(left_array)):
            result.append(left_array[index])
    if right_index < len(right_array):
        for index in range(right_index, len(right_array)):
            result.append(right_array[index])
    return result

test_array = [1, 2, 3, 4, 5, 4, 3, 2, 1, 5]

print(merge_sort(test_array))