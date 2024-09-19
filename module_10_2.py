# Задача "За честь и отвагу!":
# Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
# Атрибут name - имя рыцаря. (str)
# Атрибут power - сила рыцаря. (int)
# А также метод run, в котором рыцарь будет сражаться с врагами:
# При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
# Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
# В процессе сражения количество врагов уменьшается на power текущего рыцаря.
# По прошествию 1 дня сражения (1 секунды) выводится строка ("<Имя рыцаря> сражается <кол-во дней>..., "
#                                                            "осталось <кол-во воинов> воинов.")
# После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
# Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.
# Пункты задачи:
# Создайте класс Knight с соответствующими описанию свойствами.
# Создайте и запустите 2 потока на основе класса Knight.
# Выведите на экран строку об окончании битв.
# Алгоритм выполнения кода:
# # Создание класса
# first_knight = Knight('Sir Lancelot', 10)
# second_knight = Knight("Sir Galahad", 20)
# # Запуск потоков и остановка текущего
# # Вывод строки об окончании сражения

import threading
from time import sleep

# Класс Knight, наследуемый от Thread
class Knight(threading.Thread):
    enemies = 100  # общее количество врагов для всех рыцарей
    lock = threading.Lock()  # блокировка для синхронизации

    def __init__(self, name, power):
        super().__init__()
        self.name = name  # имя рыцаря
        self.power = power  # сила рыцаря

    def run(self):
        days = 0  # счетчик дней
        print(f"{self.name}, на нас напали!")

        while True:
            days += 1
            sleep(1)  # задержка в 1 секунду (1 день сражения)

            # Защищенный блок - синхронизированный доступ к общему количеству врагов
            with Knight.lock:
                if Knight.enemies <= 0:
                    break

                # Уменьшаем количество врагов на силу рыцаря
                Knight.enemies -= self.power
                if Knight.enemies < 0:
                    Knight.enemies = 0

                # Выводим статус сражения
                print(f"{self.name}, сражается {days} день(дня)..., осталось {Knight.enemies} воинов.")

            # Проверка на завершение сражения
            if Knight.enemies == 0:
                break

        # Финальное сообщение по завершению битвы
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


# Создаем двух рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения сражений
first_knight.join()
second_knight.join()

# Сообщение об окончании всех битв
print("Все битвы закончились!")