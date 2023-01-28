print()
print("Задача № 3: Вычислить результат выражения, с учетом приоритета действий: 12 - 4 * 2 + 6 / 3")

print()
n = input('Введите выражение для вычисления, в формате 12 - 4 * 2 + 6 / 3 :')
# "12 - 4 * 2 + 6 / 3"  ->  12 - (4 * 2) + (6 / 3) -> 12 - 8 + 2 = 6
#   0 1 2 3 4 5 6 7 8 

m1 = n.split()

print()
print (f'Делаем парсинг строки выражения, формируем список m1 иэ элементов выражения:\n{m1}')
print()

def calc (a, b, c):
    if c == "+":
        return (a + b)
    elif c == "-":
        return (a - b)
    elif c == "/":
        return round(a / b)
    elif c == "*":
        return (a * b)
m2 = []

for i in range (1, len(m1) -1, 2):
    if m1[i] == '*' or m1[i] == '/':
        result = calc(int(m1[i-1]), int(m1[i+1]), m1[i])
        m2.append(result)
    elif m1[i] == '+':
        m2.append((m1[i]))
    else: 
        m2.append(int(m1[i-1]))
        m2.append((m1[i]))
print (f'Создан новый список с промежуточным результатом m2:\n{m2}')
print()

m3 =[]

for i in range (1, len(m2) -1, 2):
    if m2[i] == '-':
        result = calc(int(m2[i-1]), int(m2[i+1]), m2[i])
        m3.append(result)
    else:
        m3.append((m2[i]))
        m3.append((m2[i+1]))

print (f'Создан новый список в промежуточным результатом m3:\n{m3}')
print()

m4 =[]

for i in range (1, len(m3) -1, 2):
        result = calc(int(m3[i-1]), int(m3[i+1]), m3[i])
        m4.append(result)

print (f'Результат вычисления выражения < {n} > с учетом приоритета действий:\n{m4}')
print()
