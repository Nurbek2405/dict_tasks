'''
Задача 4: Получение значения с методом .get()
Условие:
Напишите программу, которая пытается получить значение ключа из словаря, используя метод .get().
Если ключ отсутствует, метод должен возвращать значение по умолчанию.

my_dict = {"name": "Nurbek", "age": 29}

# Попытка получить значение по ключу
print(my_dict.get("name", "Ключ не найден"))  # Ожидаемый вывод: Nurbek
print(my_dict.get("city", "Ключ не найден"))  # Ожидаемый вывод: Ключ не найден

Ваше задание:

Создайте словарь car с ключами "brand", "model", "year" и значениями "Toyota", "Camry", 2020.
Используя метод .get(), получите значение для ключа "model", а также для отсутствующего ключа "color".
Для отсутствующего ключа укажите текст "Цвет неизвестен".

'''

'''car = {"brand": "Toyota", "model": "Camry", "year": 2020}

# Попытка получить значение по ключу
print(car.get("brand", "Ключ не найден"))  # Ожидаемый вывод: Nurbek
print(car.get("color", "Цвет неизвестен"))  # Ожидаемый вывод: Ключ не найден'''
########################################################################
'''
Задача 5: Объединение словарей
Условие:
Напишите программу, которая объединяет два словаря. Если ключи совпадают, 
значения из второго словаря заменяют значения из первого.

dict1 = {"name": "Nurbek", "age": 29}
dict2 = {"age": 30, "city": "Kokshetau"}

# Объединение словарей
dict1.update(dict2)
print(dict1)

Ваше задание:

Создайте два словаря:
person1 = {"name": "Asel", "age": 25}
person2 = {"age": 26, "city": "Almaty"}
Объедините их, чтобы данные из person2 заменили совпадающие ключи в person1. Выведите результат.
'''

'''person1 = {"name": "Asel", "age": 25}
person2 = {"age": 26, "city": "Almaty"}
person1.update(person2)
print(person1)'''
########################################################################
'''
Задача 6: Цикл по словарю
Условие:
Напишите программу, которая проходит по словарю с помощью цикла for и выводит каждую пару ключ-значение.

my_dict = {"name": "Nurbek", "age": 29, "city": "Kokshetau"}

# Цикл по словарю
for key, value in my_dict.items():
    print(f"{key}: {value}")

Ваше задание:

Создайте словарь product с ключами "name", "price", "quantity" и значениями "Laptop", 150000, 5.
Используя цикл for, выведите каждую пару ключ-значение в формате ключ: значение.
'''

'''product = {"name": "Laptop", "price": 150000, "quantity": 5}
for key, value in product.items():
    print(f"{key}: {value}")'''
########################################################################
'''
Задача 7: Подсчёт количества ключей и значений
Условие:
Напишите программу, которая подсчитывает количество ключей в словаре и выводит это число.

my_dict = {"name": "Nurbek", "age": 29, "city": "Kokshetau"}

# Подсчёт количества ключей
print(len(my_dict))  # Ожидаемый вывод: 3

Ваше задание:

Создайте словарь inventory с ключами "apples", "bananas", "oranges", "pears" и значениями 10, 20, 15, 8.
Подсчитайте количество ключей в словаре и выведите результат.
'''

'''inventory = {"apples": 10,
             "bananas": 20,
             "oranges": 15,
             "pears": 8,
             }

print(len(inventory)) '''

########################################################################
'''
Условие:
Напишите программу, которая создаёт новый словарь, где ключами становятся значения исходного словаря, а значениями — ключи.

my_dict = {"name": "Nurbek", "age": 29, "city": "Kokshetau"}

# Обратное преобразование ключей и значений
reversed_dict = {value: key for key, value in my_dict.items()}
print(reversed_dict)

Ваше задание:

Создайте словарь students с ключами "101", "102", "103" и значениями "Asel", "Ainur", "Damir".
Создайте новый словарь, где значения и ключи поменяются местами. Выведите результат.
'''

'''students = {
    "101": "Asel",
    "102": "Ainur",
    "103": "Damir",
}'''
#reversed_dict = {value: key for key, value in students.items()}
#print(reversed_dict)

########################################################################
'''
Задача 9: Создание словаря из двух списков
Условие:
Напишите программу, которая создаёт словарь, где ключи берутся из одного списка, а значения — из другого. 
Если длины списков не совпадают, лишние элементы следует игнорировать.

keys = ["name", "age", "city"]
values = ["Nurbek", 29, "Kokshetau"]

# Создание словаря из списков
result = dict(zip(keys, values))
print(result)

Ваше задание:

Создайте два списка:
keys = ["brand", "model", "year"]
values = ["Toyota", "Camry", 2020]
Создайте словарь из этих списков с помощью zip() и выведите результат.
'''

'''keys = ["brand", "model", "year"]
values = ["Toyota", "Camry", 2020]

result = dict(zip(keys, values))
print(result)

'''
########################################################################
'''
Задача 10: Подсчёт количества повторений значений
Условие:
Напишите программу, которая подсчитывает, сколько раз каждое значение встречается в словаре.

my_dict = {"name1": "Nurbek", "name2": "Asel", "name3": "Nurbek", "name4": "Damir"}

# Подсчёт количества повторений значений
value_counts = {}
for value in my_dict.values():
    value_counts[value] = value_counts.get(value, 0) + 1

print(value_counts)

Ваше задание:

Создайте словарь colors с ключами "item1", "item2", "item3", "item4", "item5" и значениями "red", "blue", "red", "green", "blue".
Подсчитайте, сколько раз каждое значение встречается в словаре, и выведите результат.
'''

'''my_dict = {"item1": "red", "item2": "blue", "item3": "red", "item4": "green"}

value_counts = {}
for value in my_dict.values():
    value_counts[value] = value_counts.get(value, 0) + 1

print(value_counts)'''

'''Условие:
Напишите программу, которая проверяет, пустой словарь или нет, и выводит соответствующее сообщение.

Входные данные:
Создайте словарь data = {}.

Подсказка:

Используйте условие if not dict_name: для проверки пустоты словаря.'''
########################################################################
'''
Задача 11: Проверка на пустоту словаря
Условие:
Напишите программу, которая проверяет, пустой словарь или нет, и выводит соответствующее сообщение.

Входные данные:
Создайте словарь data = {}.

Подсказка:

Используйте условие if not dict_name: для проверки пустоты словаря.'''
'''data = {
    'fqfq':'241412',
}
if not data:
    print('Словарь пуст.')
else:
    print('Словарь не пуст.')'''
########################################################################

'''Задача 12: Объединение нескольких словарей
Условие:
Напишите программу, которая объединяет три словаря в один. Если ключи пересекаются, значения из более позднего словаря заменяют значения из предыдущих.

Входные данные:
Создайте три словаря:

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"c": 5, "d": 6}
Подсказка:

Используйте метод .update() для последовательного объединения словарей.
Или воспользуйтесь оператором распаковки {**dict1, **dict2, **dict3} для одновременного объединения.

Ожидаемый вывод:
{'a': 1, 'b': 3, 'c': 5, 'd': 6}

'''

'''dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"c": 5, "d": 6}
dict1.update(dict2)
dict1.update(dict3)
print(dict1)'''
########################################################################
'''
Задача 13: Фильтрация словаря
Условие:
Напишите программу, которая фильтрует словарь, оставляя только те элементы, значение которых больше заданного числа.

Входные данные:
Создайте словарь scores = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88}. 
Условие фильтрации: оставить только тех, у кого значение больше 80.

Подсказка:

Используйте генератор словаря с условием: {key: value for key, value in dict_name.items() if value > threshold}.
Ожидаемый вывод:

{'Alice': 85, 'Charlie': 92, 'Diana': 88}
Продолжаем? 😊
'''

'''scores = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88}
threshold = 80

scores = {key: value for key, value in scores.items() if value > threshold}
print(scores)'''
##########################################




