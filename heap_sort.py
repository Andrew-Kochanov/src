# функция для постройки максимальной кучи
def built_heap(array, lenght, ind):

    # создание корня и потомков
    large = ind
    left = ind * 2 + 1
    right = ind * 2 +2
    
    # сравнивание корня с потомками и проверка существования потомков
    if left < lenght and array[large] < array[left]:
        large = left
    
    if right < lenght and array[large] < array[right]:
        large = right

    # если наибольший элемент не корень, меняем значения местами и делаем рекурсию
    if large != ind:
        array[ind], array[large] = array[large], array[ind]
        built_heap(array, lenght, large)


def heap_sort(array):
    lenght = len(array)

    # построение максимальной кучи, начиная с последнего узла
    for ind in range(lenght // 2 - 1, -1, -1):
        built_heap(array, lenght, ind)

    # извлечение элементов из кучи
    for ind in range(lenght - 1, 0, -1):

        # перемещаем корень в конец, т.к. это макс элемент
        array[ind], array[0] = array[0], array[ind]

        # создаем уже уменьшанную кучу
        built_heap(array, ind, 0)
    
    return array




