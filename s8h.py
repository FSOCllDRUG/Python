import menu  # менюшка


def task_1():
    print(
        'Задача 1. Напишите функцию read_last(lines, file),\n'
        'которая будет открывать определенный файл file и выводить на печать\n'
        'построчно последние строки в количестве lines (на всякий случай проверим,\n'
        'что задано положительное целое число).\n'
        'Протестируем функцию на файле «article.txt» со следующим содержимым:\n'
        'Вечерело\n'
        'Жужжали мухи\n'
        'Светил фонарик\n'
        'Кипела вода в чайнике\n'
        'Венера зажглась на небе\n'
        'Деревья шумели\n'
        'Тучи разошлись\n'
        'Листва зеленела\n'
    )
    file = enter_numbers('Введите имя файла(article.txt)', False)
    lines = enter_numbers('Сколько последних строк вывести')
    if lines > 0 and file == 'article.txt':
        solution_task_1(lines, file)
    else:
        print('Неверно указаны последние строки')


def task_2():
    print('Задача 2.\n'
          'Документ «article.txt» содержит следующий текст:\n'
          'Вечерело\n'
          'Жужжали мухи\n'
          'Светил фонарик\n'
          'Кипела вода в чайнике\n'
          'Венера зажглась на небе\n'
          'Деревья шумели\n'
          'Тучи разошлись\n'
          'Листва зеленела\n'
          'Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину\n'
          '(или список слов, если таковых несколько).\n'
          )
    file = enter_numbers('Введите имя файла(article.txt)', False)
    if file and file == 'article.txt':
        solution_task_2(file)
    else:
        print('Неверно указано название фаила')


def task_3():
    print('ДОП ЗАДАЧА.\n'
          'Классическая задача про бассейн, который заполняется через 3 трубы, слишком проста. У нас труб будет больше.\n'
          'Бассейн можно заполнить из N труб.\n'
          'В файле pipes.txt записаны времена заполнения всего бассейна только одной данной работающей трубой (в часах).\n'
          'Затем после пустой строки перечислены трубы, которые будут заполнять бассейн.\n'
          'Сколько минут на это потребуется?\n'
          'Номер трубы соответствует номеру строки, в которой записана ее производительность.\n'
          'Результат запишите в файл time.txt\n'
          'Пример\n'
          'Ввод\n'
          '1\n'
          '2\n'
          '3\n'
          '(пустая строка)\n'
          '1 2 3\n'
          'Вывод\n'
          '32.72727272727273\n'
          )
    solution_task_3()


if __name__ == "__main__":
    menu.start_menu()


def enter_numbers(text: str, output_type=True) -> int | str:
    """
    Функция ввода значения
    :param text: текст для вывода
    :param output_type: True(число) or False(строка)
    :return: default int value, or string value
    """
    value = 0
    try:
        if output_type:
            value = int(input(text + ': '))
        else:
            value = input(text + ': ')
    except:
        print('Ошибка введен текст\n')
    return value


def solution_task_1(val_one: int, val_two: str):
    """
    Функция решения первой задачи
    :param val_one: int
    :param val_two: str
    """
    with open(val_two, 'r', encoding='utf-8') as file:
        text = file.read().splitlines()
        max = len(text)
        if val_one > max:
            min = 0
            print('Не верно указано количество последних строк\n'
                  f'Будет выведен максимум в {max} строк\n'
                  )
        else:
            min = len(text) - val_one
        for e in range(min, max):
            print(text[e])
        print('\n')


def solution_task_2(val_one: str):
    """
    Функция решения второй задачи
    :param val_one: str
    """
    with open(val_one, 'r', encoding='utf-8') as file:
        text = set(file.read().split())
        text = list(sorted(text, key=len, reverse=True))
        print(text[0])
        for i in range(1, len(text)):
            if len(text[0]) == len(text[i]):
                print(text[i])
            else:
                break


def solution_task_3():
    """
    Функция решения третьей задачи
    """
    # with open('pipes.txt', encoding='utf-8') as file:
    #     time = file.read().split('\n')
    # while all(time) is False:
    #     time.remove('')
    # pipes = list(map(int, time[-1].split()))
    # time.remove(time[-1])
    # pipes = list(map(lambda x: x - 1, pipes))
    # time = [time[pipe] for pipe in pipes]
    # with open('time.txt', 'w', encoding='utf-8') as answer:
    #     answer.write(str(60 / sum(map(lambda x: 1 / float(x), time))))

    f = open('pipes.txt', 'r')
    f2 = open("time.txt", "w")
    s = [line.rstrip() for line in f]
    d = []
    d1 = []
    flag = 0
    for i in s:
        if flag == 0:
            if i != '':
                d.append(eval(i))
            else:
                flag += 1
        else:
            s1 = i.split()
            for j in s1:
                d1.append(d[int(j) - 1])
    f2.write(str(60 / sum([1 / i for i in d1])))
    f2.close()
    f.close()
