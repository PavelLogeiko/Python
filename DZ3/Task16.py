#Задача 16:
#Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
#Заполните массив случайными натуральными числами от 1 до N/2.
#Выведите, сколько раз X встречается в массиве.
#Пример:
#Ввод: 5 длина массива
#Ввод: 1 число
#Массив 1 2 1 2 2
# Вывод: 2

print ("")
print ("Задача: Задать массив от 1 до N/2 и выяснить какое количество раз в массиве встречается X.")
print ("")

n = int (input("Введите число N: "))
print ("")
m = round(n/2)
x = int (input ("Введите число X: "))
print ("")
arr = []
from random import randint

if n <=0:
    print ("Вы ввели значение числа N равное 0 или отрицательное число, попробуйте снова :)")

else:
    for _ in range(n):
        arr.append(randint(1, m))
    print ("Задан массив: ")
    print ("")
    print(arr)
    print ("")
    print("Заданное число X встречается в массиве раз:", arr.count(x))
print ("")