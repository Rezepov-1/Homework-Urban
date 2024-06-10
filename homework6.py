my_dict = {"Timur": 35, "Amir": 7, "Marat": 30}
print("Справочник:", my_dict)
print("Поиск [Амир]:", my_dict.get("Amir"))
print("Поиск [Камилла]:", my_dict.get("Kamilla"))
my_dict.update({"Rustam": 66,"Kamilla": 5})
my_dict.pop("Timur")
print(my_dict)

my_set = {35, "разве", "это", "возраст",  True, 35, "разве", "нет", "конечно"}
print("Set", my_set)
my_set.update({"вот это новость", False})
print(my_set.discard("нет"))
print("Modified set:", my_set)