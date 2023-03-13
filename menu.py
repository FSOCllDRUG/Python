import s8h

menu_options = {
    1: 'Задача 1',
    2: 'Задача 2',
    3: 'Задача 3',
    4: 'Exit',
}


def print_menu():
    """
    Функция отрисовки меню в консоль
    :return:
    """
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def start_menu():
    """
    Основная функция запуска программы.
    :return:
    """
    while (True):
        print_menu()
        task = ''
        try:
            task = int(input('Введите от 1 до 5: '))
        except:
            print('Введите номер задачи.')
        # Проверка введённого числа и запуск функции в основном фаиле
        if task == 1:
            s8h.task_1()
        elif task == 2:
            s8h.task_2()
        elif task == 3:
            s8h.task_3()
        elif task == 4:
            print('Выходим из программы')
            exit()
        else:
            print('Ошибка. Введите от 1 до 4.')