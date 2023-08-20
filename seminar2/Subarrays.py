# Напишите функцию, которая принимает массив чисел и значение X. 
# Функция должна возвращать массив подмассивов так, 
# чтобы сумма чисел в каждом подмассиве была меньше или равна X.
def split_array(array, max_sum):
    sorted_array = sorted(array)
    arrays = [] # массив подмассивов
    sub_array = [] # подмассив
    sum = 0
    for value in sorted_array:
        if sum + value > max_sum:
            arrays.append(sub_array)
            sub_array = []
            sum = 0
        sub_array.append(value)
        sum += value
        if value > max_sum:
            break
    return arrays

if __name__ == "__main__":
    array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(split_array(array, 7))
            
            

