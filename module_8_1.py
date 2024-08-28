# Реализуйте следующую функцию:
# add_everything_up, будет складывать числа(int, float) и строки(str)
#
# Описание функции:
# add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float), так и строками(str).
# TypeError - когда a и b окажутся разными типами (числом и строкой),
# то возвращать строковое представление этих двух данных вместе (в том же порядке).
# Во всех остальных случаях выполнять стандартные действия.
#
# Пример кода:
# print(add_everything_up(123.456, 'строка'))
# print(add_everything_up('яблоко', 4215))
# print(add_everything_up(123.456, 7))

def add_everything_up(a, b):
    try:
        # Попробуем сложить a и b, если они одного типа
        result = a + b
    except TypeError:
        # Если типы разные, возвращаем строковое представление
        result = str(a) + str(b)
    return result

# Пример кода:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))