# Чистые функции и неизменяемость данных: Напишите функцию, которая принимает список чисел 
# и возвращает новый список, в котором каждый элемент умножен на 2. 
# Убедитесь, что вы используете только чистые функции и не изменяете исходный список.

def doubled_list(list):
    return [x * 2 for x in list]

test_list = [1, 2, 3, 4, 5]

print(doubled_list(test_list))
print(test_list)