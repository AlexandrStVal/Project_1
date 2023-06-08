list_of_numbers = list(map(int, input("Введите числа через пробел: ").split()))  # список чисел
free_num = int(input('Введите число: '))
# функция сортирует список по возрастанию
def list_sort(nums):
    for item in range(len(nums)):
        min_index = item  # как наименьший элемент
        for j in range(item + 1, len(nums)):  # цикл перебирает несортированные элементы
            if nums[j] < nums[min_index]:
                min_index = j
        # меняем самый низкий несортированный элемент с первым несортированным
        nums[item], nums[min_index] = nums[min_index], nums[item]
# запуск функции
list_sort(list_of_numbers)
print(set(list_of_numbers))
print('_______')

# # Двоичный поиск требует сортировки элементов в списке
def binary_search(data, elem, low, high):
    if data[-1] < elem:
        return 'Введенное число больше максимального в списке!'
    elif data[0] > elem:
        return 'Введенное число меньше минимального в списке!'
    elif data[0] == elem:
        return 'Введенное число равно минимальному в списке!'

    while high - low > 1:
        middle = (low + high) // 2
        if data[middle] >= elem:
            high = middle
        else:
            low = middle
    return (f'Индекс числа, меньшего введенному числу: {low}.\nИндекс числа, большего (равного) введенному числу: {high}.')
print(binary_search(list_of_numbers, free_num, 0, len(list_of_numbers)))