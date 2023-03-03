#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#Пример:
#5
#1 2 3 4 5
#6
#-> 5

from random import randint
array = [randint(1, 99) for i in range(int(input('Введите размер массива: ')))]
print(array)
num = int(input('Введите искомое число: '))
array = set(array)
dif = 0
if num > max(array):
    print(max(array))
elif num < min(array):
    print(min(array))
else:
    while True:
        if num - dif in array and num + dif in array and num - dif != num + dif:
            print(num - dif, num + dif)
            break
        elif num - dif in array:
            print(num - dif)
            break
        elif num + dif in array:
            print(num + dif)
            break
        else:
            dif += 1