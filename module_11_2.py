# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента
# и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль,
# и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#   - Тип объекта.
#   - Атрибуты объекта.
#   - Методы объекта.
#   - Модуль, к которому объект принадлежит.
#   - Другие интересные свойства объекта, учитывая его тип (по желанию).
#
#
# Пример работы:
# number_info = introspection_info(42)
# print(number_info)


def introspection_info(obj):
    # Словарь для хранения информации
    info = {}

    # Определение типа объекта
    info['type'] = type(obj).__name__

    # Модуль, к которому объект принадлежит
    info['module'] = getattr(obj, '__module__', 'Built-in')  # Некоторые объекты встроены и не имеют модуля

    # Атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    info['attributes'] = attributes

    # Методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]
    info['methods'] = methods

    return info


number_info = introspection_info(42)
print(number_info)