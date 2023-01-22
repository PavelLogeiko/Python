import function as f
# меню

file_bus = 'bus.txt'
file_driver = 'driver.txt'
file_rout = 'rout.txt'

class Menu:

    menuitems = '''1 - Вывод автобусов\n2 - Добавление автобуса\n3 - Вывод водителя\n4 - Добавление водителя\n5 - Вывод маршрута\n6 - Добавление маршрута\n7 - Выход'''
    while (True):
        print ()
        print ('Меню справочника:'+ '\n')
        print(menuitems)
        answer = input('>:')
        print()
        match answer:
            case "1":
                # Вывод автобусов
                print(f.print_bus(file_bus))
            case "2":
                # Добавление автобуса
                f.add_bus(file_bus)
            case "3":
                # Вывод водителей
                print(f.print_driver(file_driver))
            case "4":
                # Добавление водителя
                f.add_driver(file_driver)
            case "5":
                # Вывод маршрута
                print(f.print_rout(file_rout))
            case "6":
                # Добавление маршрута
                f.add_rout(file_rout)
            case "7":
                # Выход
                exit(0)
            case _:
                print('Неверный ввод')
                exit(0)
