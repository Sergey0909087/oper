# создание списка
# numbers = [2, 4, 6, 8, 10]
# languages = ['Python', 'C#', 'C++', 'Java']
#
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(numbers[4])
# print(numbers[5])
# print()
# print(languages[0])
# print(languages[1])
# print(languages[2])
# print(languages[3])
# print()
# info = ['Python', 2023, 24.2, True]
# print(info[0])
# print(info[1])
# print(info[2])
# print(info[3])

# Создание пустого списка
# list_1 = []
# list_2 = list()
# print(list_1)
# print(list_2)
#
# list_3 = [1, 2, 3, 4, 5]
# print(list_3)

# Функция list()
# numbers = list(range(5))
# print(numbers)
#
# even_numbers = list(range(0, 10, 2))
# print(even_numbers)
# odd_numbers = list(range(1, 10, 2))
# print(odd_numbers)

# s = 'abcde!! , 123'
# chars = list(s)
# print(chars)

# Вложенные списки
# numbers = [[1, 2, 3], [4, 5, 1234]]
# print(numbers)
# print(numbers[1])
# print(numbers[1][2])
# print(str(numbers[1][2])[2])

# Сходства
# len() - возращает размер списка
# in - оператор пренадлежности
# word = [1, 2, 3, 4, 'hello', 5, 'pencil']
# if 'pen' in word:
#     print('YES')
# list_1 = [1, 2, 3, 4, 5]
# print(max(list_1))
# print(min(list_1))
# print(sum(list_1))

# Методы списков
# append - добавить в конец списка
# remove - удалить первый совпадающий элемент списка
# pop - удалить элемент по индексу с возможностью сохранить значение в переменной
# clear - очистить список
# sort - сортирует список
# extend - обьединить списки
# insert - вставить элемент по индексу

# new_list = [1, 2, 2, 3, 4]
# print(new_list)
# new_list.append(5)
# print(new_list)
# new_list.append([1, 2, 3])
# print(new_list)
#
# new_list.remove(2)
# print(new_list)
#
# element = new_list.pop(5)
# print(new_list)
# # print(element)
#
# var = new_list.pop()
# print(new_list)
# print(var)
#
# new_list.clear()
# print(new_list)

# list_1 = [4234, 123, 456, 23, 58, 978, 456, 345]
# list_2 = ['Python', 'C#', 'C++', 'Java']
# print(list_1)
# print(list_2)
#
# list_1.sort()
# list_2.sort()
#
# print(list_1)
# list_1.sort(reverse=True)
# print(list_1)
# print(list_2)
# list_2.sort(reverse=True)
# print(list_2)

# list_1 = [1, 2, 3]
# list_2 = [3, 4, 5]
# list_1.extend(list_2)
# print(list_1)
# print(list_1 + list_2)

# print(list_1)
# list_1.insert(1, 10)
# print(list_1)
# list_1.insert(3, 'PYTHON')
# print(list_1)

# Кортеж (не изменяемый список)
# a = ()
# print(a)
# a = (3, )
# print(type(a))

# a = (1, 2, 3)
# print(a)
# a = list(a)
# print(a)
# a.append(4)
# print(a)
# a = tuple(a)
# print(a)

# numbers = list(range(5))
# print(numbers)
#
# even_numbers = list(range(0, 10, 2))
# print(even_numbers)
# odd_numbers = list(range(1, 10, 2))
# print(odd_numbers)


a = []
i = 0
while len(a) < 45:
    if i % 2 == 0:
        a.append(i)
    i += 1
print(a)
print(len(a))