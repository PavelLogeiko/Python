#Задача 22:
#Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа.
#n - кол-во элементов первого набора.
#m - кол-во элементов второго набора.
#Значения генерируются случайным образом.
#Пример:
#Ввод: 11 6
#(значения сгенерированы случайным образом
#2 4 6 8 10 12 10 8 6 4 2
#3 6 9 12 15 18)
#Вывод: 6, 12

print ("")
print ("Задача: Задать два массива [1 .. N / M], размерами (N) и (M), выдать в порядке возрастания все числа, которые встречаются в обоих наборах.")
print ("")

n = int (input("Введите число N > 0: "))
print ("")
m = int (input ("Введите число M > 0: "))
print ("")
arr_1 = []
arr_2 = []
from random import randint

for _ in range(n):
    arr_1.append(randint(1, n))
print ("Задан массив № 1: ")
print ("")
print (arr_1)
print ("")

for _ in range(m):
    arr_2.append(randint(1, m))
print ("Задан массив № 2: ")
print ("")
print (arr_2)
print ("")

new_arr_1 = []

if n >= m:
    for i in range(1, n+1):
        if (i in arr_1) and (i in arr_2):
            new_arr_1 += [i]
else:
    for i in range(1, m+1):
        if (i in arr_1) and (i in arr_2):
            new_arr_1 += [i]

print ("Числа в порядке возрастания в обоих массивах: ")
print ("")           
print (new_arr_1)
print ("")
