immutable_var = (11, "один", 3.14, True)
print( "Immutable tuple:", immutable_var)
# Попытка изменить элементы кортежа immutable_var
# Ошибка
# Объяснение: Кортежи в Python являются неизменяемыми структурами данных.
# Это означает, что после создания кортежа его элементы нельзя изменить, добавить или удалить.
mutable_list = [11, "один", 3.14, True]
mutable_list[0] = "Синергия"
mutable_list[1] = 1
mutable_list[2] = "число пи"
mutable_list[3] = False
print("Mutable list:", mutable_list)