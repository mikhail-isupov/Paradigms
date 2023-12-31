# Функции высшего порядка: Создайте функцию высшего порядка, которая принимает другую функцию и список чисел.
# Функция высшего порядка должна возвращать список, содержащий результаты применения переданной функции к каждому элементу списка.
def my_map(func, list):
    return [func(x) for x in list]

test_list = [1, 2, 3, 4, 5]

def test_func(x):
    return x * x

print(my_map(test_func, test_list))