arr = [1, 5, -10, 2, 4, 9, -3, 10]
print(arr)

# 1. Найти сумму отрицательных элементов массива.


def find_negative_num_sum(array):
    negative_num_sum = []
    for i in array:
        if i < 0:
            negative_num_sum.append(i)

    return sum(negative_num_sum)


print(find_negative_num_sum(arr))


# 2. Найти произведение элементов массива, расположенных между максимальным и минимальным элементами.


def find_multiplication_between_max_and_min(array):
    mul = 1
    min_num, max_num = min(array), max(array)
    index_min, index_max = array.index(min_num), array.index(max_num)
    print(f'Индекс минимального элемента массива - {index_min}, индекс максимального элемента массива - {index_max}')
    if index_min > index_max:
        for i in array[index_max + 1: index_min]:
            mul *= i
    else:
        for i in array[index_min + 1: index_max]:
            mul *= i
    return mul


print(find_multiplication_between_max_and_min(arr))


# 3. Упорядочить элементы массива по убыванию

sorted_arr = sorted(arr)
print(sorted_arr[::-1])