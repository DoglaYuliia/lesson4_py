# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

my_list = [34, 65, 123, 495, 1, 495, 37, 33, 777]

for symbol in my_list:
    if symbol > 100:
        print(symbol)

#############################
# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.

my_list = [34, 65, 123, 495, 1, 495, 37, 33, 777]
my_results = []

for symbol in my_list:
    if symbol > 100:
        my_results.append(symbol)
print(my_results)

#############################
# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух
# элементов.Количество элементов в списке можно получить с
# помощью функции len(my_list)

my_list = [34, 65, 123, 495, 1, 495, 37, 10, 20]

if len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
    print(my_list)
else:
    my_list.append(0)
    print(my_list)

#############################
# 4) У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и поместить их в список.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и
# приведение типов.Генерирование через range или другие "фишки"
# я засчитывать не буду ))

my_string = '0123456789'
new_list = []
for symbol1 in my_string:
    for symbol2 in my_string:
        new_list.append(int(symbol1 + symbol2))
print(new_list)
