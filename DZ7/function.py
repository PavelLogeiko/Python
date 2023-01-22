file_bus = 'bus.txt'
file_driver = 'driver.txt'
file_rout = 'rout.txt'

def print_bus(file_bus):
    print('Перечень автобусов автопарка: ' + '\n')
    result = []
    with open(file_bus, "r+", encoding="utf8") as datafile:
        for line in datafile:
            result.append(line.split())
        return result


def add_bus(file_bus):
    new_line = input('Добавьте автобус в указанном формате (без < >), через пробел и нажмите Enter - < ID Автобуса Госномер> (пример: bus1 В789ОВ178)>\nили нажмите Enter - для выхода в меню:')
    if new_line == "": return
    with open (file_bus, 'a', encoding = 'utf8') as data:
        data.writelines ('\n'+ new_line)


def print_driver(file_driver):
    print('Перечень водителей автопарка: ' + '\n')
    result = []
    with open(file_driver, "r+", encoding="utf8") as datafile:
        for line in datafile:
            result.append(line.split())
        return result


def add_driver(file_driver):
    new_line = input('Добавьте водителя в указанном формате (без < >), через пробел и нажмите Enter - < ID Водителя Фамилия> (пример: driver1 Ivanov)>\nили нажмите Enter - для выхода в меню:')
    if new_line == "": return
    with open (file_driver, 'a', encoding = 'utf8') as data:
        data.writelines ('\n'+ new_line)


def print_rout(file_rout):
    print('Перечень маршрутов автопарка: ' + '\n')
    result = []
    with open(file_rout, "r+", encoding="utf8") as datafile:
        for line in datafile:
            result.append(line.split())
        return result


def add_rout(file_rout):
    new_line = input('Введите маршрут в указанном формате (без < >), через пробел и нажмите Enter - < Номер маршрута Километраж Автобус Водитель (пример: m1 5 bus1 driver1)>\nили нажмите Enter - для выхода в меню:')
    if new_line == "": return
    with open (file_rout, 'a', encoding = 'utf8') as data:
        data.writelines ('\n'+ new_line)
