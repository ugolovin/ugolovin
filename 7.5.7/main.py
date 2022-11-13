
def merge_sort(array): #Сортировка реализованна алгоритмом "Сортировка слиянием", в виде двух функций "merge_sort","merge"
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def binary_search(array, element, left, right): #Функция двоичного поиска.
    middle = (right + left) // 2

    if left > right:
        return middle #Возвращает номер элемента который меньше введённого числа, но при этом рядом с ним.

    if array[middle] == element:
        return middle
    elif element < array[middle]:

        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


def input_true(): #Функция проверки условии ввода данных.
    try:
        print("Введите последовательность чисел через пробел:")
        array = str.split(input())
        for i in range(len(array)):
            array[i] = float(array[i])
        if len(array) <= 1:
            raise ValueError

        print("Введите любое число:")
        element = float(input())

        return array, element

    except ValueError:
        print("Ошибка!!! Введены неверные данные!")
        exit()


array, element = input_true()

array = merge_sort(array)
print("Отсортированная последовательность по возрастанию элементов в ней:")
print(array)

if element < array[0]:
    print("Введённое число:", element, " не подходит. Оно меньше минимального числа введённой последовательности:", array[0]) # Нету числа "слева", поэтому не подходит по заданию.
elif element > array[len(array)-1]:
    print("Введённое число:", element, " не подходит. Оно больше максимального числа введённой последовательности:", array[len(array) - 1]) # Нету числа "справа", поэтому не подходит по заданию.
else:
    middle_id = binary_search(array, element, 0, len(array) - 1)
    print("Номер позиции элемента, который меньше введенного пользователем числа,а следующий за ним больше или равен этому числу:", middle_id,"\n")


