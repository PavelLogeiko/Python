# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P
# Помогите Кате отгадать задуманные Петей числа.
# Пример: 
# 4, 4 >> 2, 2
# 5, 6 >> 2, 3
#

print ("")
print ("Задача: выяснить значения чисел, для которых известны их сумма и произведение.")
print ("")
s = int (input ("Введите значение суммы искомых чисел: "))
p = int (input ("Введите значение произведения искомых чисел: "))
print ("")
print ("Заданы числа,","сумма:",f'{s}', "произведение:",f'{p}')
c = 0
for i in range(s + p):
    if c:
        break
    for j in range(s + p):
        if i + j == s and i * j == p:
            c = 1
            print ("Искомые числа: " f'{i}',"и", f'{j}')
            break
else:
    print ("Для заданных суммы и произведения нет подходящих по условию чисел, попробуйте ввести другие значения:) ")
print ("")