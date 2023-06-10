# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

list_1 = [1, 6, 19, 2, 41, 12, 77, 92, 45, 5, 1, 6]
list_2 = [40, 12, 87, 2, 6, 14, 99, 7, 2, 12, 6]
list_3 = set()

for i in list_1:
    for k in list_2:
        if i == k:
            list_3.add(i)

print(list_3)
list_3 = list(list_3)
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort(list_3))