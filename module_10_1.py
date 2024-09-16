# Задача "Потоковая запись в файлы":
# Необходимо создать функцию wite_words(word_count, file_name), где word_count - количество записываемых слов,
# file_name - название файла, куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>"
# в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
# Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
#
# После создания файла вызовите 4 раза функцию wite_words, передав в неё следующие значения:
# 10, example1.txt
# 30, example2.txt
# 200, example3.txt
# 100, example4.txt
# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
# 10, example5.txt
# 30, example6.txt
# 200, example7.txt
# 100, example8.txt
# Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
# Также измерьте время затраченное на выполнение функций и потоков.
# Как это сделать рассказано в лекции к домашнему заданию.

import threading
from time import sleep, time


# Функция для записи слов в файл
def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


# Вызов функции 4 раза без потоков
def sequential_execution():
    print("Запуск последовательных вызовов функций")
    start_time = time()

    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")

    end_time = time()
    print(f"Последовательное выполнение заняло {end_time - start_time} секунд")


# Функция для запуска функций в потоках
def threaded_execution():
    print("Запуск функций в потоках")
    start_time = time()

    # Создаем потоки
    thread1 = threading.Thread(target=write_words, args=(10, "example5.txt"))
    thread2 = threading.Thread(target=write_words, args=(30, "example6.txt"))
    thread3 = threading.Thread(target=write_words, args=(200, "example7.txt"))
    thread4 = threading.Thread(target=write_words, args=(100, "example8.txt"))

    # Запускаем потоки
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    # Ждем завершения потоков
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    end_time = time()
    print(f"Выполнение с потоками заняло {end_time - start_time} секунд")


# Запуск последовательного выполнения
sequential_execution()

# Запуск выполнения с потоками
threaded_execution()