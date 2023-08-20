# Задание: Создайте функцию, которая принимает двумерный массив (лабиринт) и начальную и конечную точки.
# Функция должна возвращать путь от начальной до конечной точки или сообщение, что путь невозможен.
# Входные данные:
# Двумерный массив размера MxN, где '0' - это проход, а '1' - это стена.
# Координаты начальной и конечной точки.

def maze_search(labyrinth, start_row = 0, start_column = 0, end_row = 0, end_column = 0):
    row = start_row
    column = start_column
    vector = [0, 1] # Направление движения
    trajectory = [[start_row, start_column]] # Путь обхода лабиринта
    attempts = 3 # Сколько раз нужно вернуться в исходную точку, чтобы прекратить поиски пути
    # тут нужно добавить проверку что исходная точка внутри массива 

    while attempts and (row != end_row or column != end_column): # Ишем, пока не исчерпаем все попытки
        # или не придем в конечную точку
        
        new_row = row + vector[0]
        new_column = column + vector[1] # что впереди
        left_row = row - vector[1]
        left_column = column + vector[0] # что слева
        if left_row < 0 or left_column < 0 or left_row > len(labyrinth) - 1 or left_column > len(labyrinth[left_row]) - 1 or labyrinth[left_row][left_column]: # Если слева стена
            if new_row < 0 or new_column < 0 or new_row > len(labyrinth) - 1 or new_column > len(labyrinth[new_row]) - 1 or labyrinth[new_row][new_column]: # Если впереди стена
                vector[0], vector[1] = vector[1], -vector[0] # поворот вправо
            else:
                row = new_row
                column = new_column # шаг вперед
                trajectory.append([row, column]) # добавляем текущую точку траектории
        else:
            row = left_row
            column = left_column
            vector[0], vector[1] = -vector[1], vector[0] # шаг влево и поворот налево
            trajectory.append([row, column]) # добавляем текущую точку траектории

        if row == start_row and column == start_column:
            trajectory = [[start_row, start_column]]
            attempts -= 1
        
            
    return trajectory # Если путь не найден возврашается список с единственной начальной координатой

if __name__ == "__main__":
    labyrinth = [[0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 1, 1, 0],
                 [1, 1, 0, 0, 0]]
    
    trajectory = maze_search(labyrinth, 0, 0, 3, 3) # Это список координат
    print(trajectory) 

    for coordinate in trajectory:
        labyrinth[coordinate[0]][coordinate[1]] = 7 # Визуализация пути по лабиринту
    
    for row in labyrinth:
        print(row)


    