# Создать телефонный справочник, с возможностью выполнения действий по меню:
# 1 - Вывод записей
# 2 - Добавление записи
# 3 - Поиск записи
# 4 - Удаление записи
# 5 - Выход 

import re

fileName = 'Telefon.txt'

# функция добавления записи
def writeFile(fileName):
    new_line = input('Введите строку в указанном формате (без < >), через пробел и нажмите Enter - < Фамилия Имя Отчество +79111234567 >\nили нажмите Enter - для выхода в меню:')
    if new_line == "": return
    with open (fileName, 'a', encoding = 'utf8') as data:
        data.writelines ('\n'+ new_line)

# функция чтения записей
def readFile(fileName):
    result = []
    with open (fileName, 'r+', encoding = 'utf8') as data:
        for line in data:
            result.append (line.split())
        return result

# функция поиска записи
def readUser (userList):
    last_name = input('Введите Фамилию для поиска номера телефона или нажмите Enter - для выхода в меню: ')
    if last_name == "": return
    for user in userList:
        if user[0] == last_name:
            print('Для введенной Фамилии, найден номер телефона:' + '\n')
            print(user[0], user[1], user[2], user[3])

# функция удаления записи
def deleteUser (fileName):
    last_name = input('Введите Фамилию контакта, запись о котором хотите удалить или нажмите Enter - для выхода в меню: ')
    if last_name == "": return
    f = open(fileName, "r+", encoding = 'utf8')
    Lines = f.readlines()
    f.seek(0)
    for line in Lines:
        if not re.search(last_name, line):
            f.write(line)
    f.truncate()
    f.close()
    print('Запись для указанного контакта удалена из телефонного справочника.')

# меню
menu = '''1 - Вывод записей\n2 - Добавление записи\n3 - Поиск записи\n4 - Удаление записи\n5 - Выход '''
while (True): 
    print ()
    print ('Добро пожаловать в телефонный справочник, выберите действие:'+ '\n')
    print(menu)
    answer = input('>:')
    print()
    match answer:
        case "1":
            # вывод записей
            print('В телефонном справочнике содержаться следующие записи:' + '\n')
            print(readFile(fileName))
        case "2":
            # добавление записи (данных)
            writeFile(fileName)
        case "3":
            # поиск записи (данных)
            readUser(readFile(fileName))
        case "4":
            # удаление записи (данных)
            deleteUser(fileName)
        case "5":
            # выход
            exit(0)
        case _:
            print('Неверный ввод')
            exit(0)
