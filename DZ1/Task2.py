#Задача 2
#Найдите сумму цифр трехзначного числа.
#Пример:
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

print ("")
print ("Задача: Найти сумму чисел трехзначного числа.")
print ("")
x = int (input ("Введите целое трехзначное число: "))
print ("")

if x <=99 or x >= 1000:
    print ("Вы ввели не трехзначное число, попробуйте снова :)")
else:
    first = x // 100
    second = x // 10 % 10
    third = x % 10
    sum = first + second + third
    print ("Сумма трехзначного числа: " f'{first}', '+', f'{second}','+', f'{third}', '=', f'{sum}')
print ("")