# Цель: закрепить знания множественного наследования в Python.
# Задача "Мифическое наследование":
# Необходимо написать 3 класса:
# Horse - класс описывающий лошадь. Объект этого класса обладает следующими атрибутами:
# x_distance = 0 - пройденный путь.
# sound = 'Frrr' - звук, который издаёт лошадь.
# И методами:
# run(self, dx), где dx - изменение дистанции, увеличивает x_distance на dx.
#
# Eagle - класс описывающий орла. Объект этого класса обладает следующими атрибутами:
# y_distance = 0 - высота полёта
# sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)
# И методами:
# fly(self, dy) где dy - изменение дистанции, увеличивает y_distance на dy.
#
# Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
# Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.
# Также обладает методами:
# move(self, dx, dy) - где dx и dy изменения дистанции.
# В этом методе должны запускаться наследованные методы run и fly соответственно.
# get_pos(self) возвращает текущее положение пегаса в виде кортежа
# - (x_distance, y_distance) в том же порядке.
# voice - который печатает значение унаследованного атрибута sound.
# Пункты задачи:
# Создайте классы родители: Horse и Eagle с методами из описания.
# Создайте класс наследник Pegasus с методами из описания.
# Создайте объект класса Pegasus и вызовите каждый из ранее перечисленных методов, проверив их работу.


# Класс Horse, описывающий лошадь
class Horse:
    def __init__(self):
        self.x_distance = 0  # Пройденный путь
        self.sound = 'Frrr'  # Звук, который издает лошадь

    def run(self, dx):
        self.x_distance += dx  # Увеличиваем пройденный путь


# Класс Eagle, описывающий орла
class Eagle:
    def __init__(self):
        self.y_distance = 0  # Высота полета
        self.sound = 'I train, eat, sleep, and repeat'  # Звук, который издает орел

    def fly(self, dy):
        self.y_distance += dy  # Увеличиваем высоту полета


# Класс Pegasus, который наследуется от Horse и Eagle
class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)  # Инициализация Horse
        Eagle.__init__(self)  # Инициализация Eagle

    def move(self, dx, dy):
        self.run(dx)  # Запускаем метод run от Horse
        self.fly(dy)  # Запускаем метод fly от Eagle

    def get_pos(self):
        return (self.x_distance, self.y_distance)  # Возвращаем текущее положение

    def voice(self):
        print(self.sound)  # Печатаем звук (sound) от Eagle


# Проверка работы классов
p1 = Pegasus()

print(p1.get_pos())  # (0, 0)
p1.move(10, 15)
print(p1.get_pos())  # (10, 15)
p1.move(-5, 20)
print(p1.get_pos())  # (5, 35)

p1.voice()  # I train, eat, sleep, and repeat