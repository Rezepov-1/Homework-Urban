# 1.Функция с параметрами по умолчанию
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

#2.Распаковка параметров:
def print_params(a, b, c):
    print(a, b, c)
values_list = [5, 'оценка', True]
values_dict = {'a': 178, 'b': (1, 33, 55), 'c': 'всё это какие-то ключи'}
print_params(*values_list)
print_params(**values_dict)

#Распаковка + отдельные параметры:
def print_params(a, b, c):
    print(a, b, c)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

