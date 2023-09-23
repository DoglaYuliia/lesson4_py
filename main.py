#  игра угадай число

from random import randint

# comp_value = randint(1, 10)
# print(comp_value)

min_limit = 1
max_limit = 100

# cur_value = int(input(f"Угадай число от {min_limit} до {max_limit}: "))
# while cur_value != comp_value:
#
#     # case_word = "меньше: " if cur_value > comp_value else "больше: "
#     # cur_value = int(input(f"попробуй число {case_word}"))
#
#     if cur_value > comp_value:
#         cur_value = int(input("попробуй меньше: "))
#     else:
#         cur_value = int(input("попробуй больше: "))
# print("победа")



#обработка исключений

# value = input('Введи целое число: ')
#
# try:
#     value_int = int(value)
#     result = 1 / value_int
#     print(result)
# except ValueError:
#     print('Это не число')
# except ZeroDivisionError:
#     print('на ноль делить нельзя')


###################  ЦИКЛ FOR #####################

my_str = 'qAuerty1n2 3@ ^&'

# for symbol in my_str:
#     if symbol.isalnum() and symbol != ' ':
#         print(symbol)


# for symbol in my_str:
#     if symbol.lower() in 'eyuioa':
#         print(symbol)

###################  Кортежи и списки #####################
#итерируемые объекты
my_tuple = (1, -10, 'qwe', True, 3.14, (-2, 0), ['a', 'z'])  # не изменяемый тип
my_list = [1, -10, 'qwe', True, 3.14, (-2, 0), ['a', 'z']]   # изменяемый тип

print(my_tuple, type(my_tuple))
print(my_list, type(my_list))

index = -1
print(my_tuple[index], my_list[index])

print(len(my_tuple), len(my_list))

new_list = my_list[1:-1]
print(my_list)

new_tuple = my_tuple[::-1]
#print(new_tuple)


for value in my_list:
    if type(value) == int:
        print(value)


# замена элемента в списке
my_list[0] = 100
print(my_list)

#  в кортеже возможна замена созданием нового кортежа
my_tuple = (100, *my_tuple[1:])
print(my_tuple)


# распаковка кортежей и списков
val_1 = 12
val_2 = 21
val_1, val_2 = val_2, val_1
print(val_1, val_2)

item = val_2, val_1
print(item, type(item))
val_1, val_2 = item
print(val_1, val_2)

my_tuple = (1, 2, 'qwe')
val_int_1, val_int_2, _ = my_tuple  # заглушка
print(val_int_1, val_int_2, _)


my_tuple = (1, -10, 'qwe', True, 3.14, (-2, 0), ['a', 'z'])  # не изменяемый тип
my_list = [1, -10, 'qwe', True, 3.14, (-2, 0), ['a', 'z']]

# my_list[-1] = 100
# print(my_list)

my_list[-1][0] = 100
print(my_list)


# 1 2
# 3 4
my_table = [1, 2], [3, 4]
my_table[1][1] = 24
print(my_table)


my_tuple2 = (1, 2, 3)
print((id(my_tuple2), id))

#####################################
#####################################

new_list1 = []

for symbol in 'qwerty':
    new_list1.append(symbol)
new_list1.append(1000)
print(new_list1)
new_list.pop(0)
print(new_list1)

#######

new_tuple2 = list(('qwerty', 'xgfghjk'))
new_list2 = list(new_tuple2)
new_list2[0] = 123
print(new_list2)
new_tuple3 = tuple(new_list2)
print(new_tuple3)

###########

new_list3 = list('new_tuple')
print(new_list3)

new_str = '$'.join(new_list3)
print(new_str)

new_str = ''.join(new_list3)
print(new_str)

###############

# filename = "lesson4_py.py.txt"
# filename = filename.replace(".txt", "")
# print(filename)

filename = "lesson4_py.py.docs"
# filename_parts = filename.split(".")
# print(filename_parts)
# filename = ".".join(filename_parts[:-1])
# print(filename)


filename = filename.rsplit(".", 1)[0]
print(filename)