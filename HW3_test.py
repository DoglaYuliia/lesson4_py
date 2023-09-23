values = [1, 2, 3, 4, 5]
print(type(values))

#######################
values = (1, 2, 3, 4, 5)
print(type(values))

#######################
values = (1, 2, 3, 4, 5)
values = list(values)
print(type(values))

#######################
values = [1, 2, 3, 4, 5]
values = tuple(values)
print(type(values))

#######################
values = [1, 2, 3, 4, 5]
result = []

for value in values:
    result.append(value)
print(result)

#######################
values = [1, 2, 3, 4, 5]
result = []
for value in values[::-1]:
    result.append(value)
print(result)

#######################
values = [1, 2, 3, 4, 5]
print(len(values))

#######################
values = [1, 2, 3, 4, 5]
new_value = values + values[::-1]
print(new_value)

#######################
values = [1, 2, 3, 4, 5]
new_value = values
new_value.append(6)
print(values)

#######################
values = [1, 2, 3, 4, 5]
new_value = values.copy()
new_value.append(6)
print(values)

#######################
values = [0] * 6
values[0] = 1
print(values)

#######################
value = 0
values = [value] * 6
print(values)

#######################
my_list = [0]
values = [my_list] * 3
print(values)

#######################
my_list = [0]
values = [my_list] * 3
my_list.append(1)
print(values)

#######################
my_list = [0]
values = [my_list.copy()] * 3
my_list.append(1)
print(values)

#######################
my_list = ['a', 'b', 'c', 'd', 'e', 'f']
my_str = " ".join(my_list)
print(my_str)

#######################
my_list = ['a', 'b', 'c', 'd', 'e', 'f']
my_str = "_".join(my_list)
print(my_str)

#######################
my_list = ['a', 'b', 'c', 'd', 'e', 'f']
my_str = "_".join(my_list[::-1])
print(my_str)

#######################
my_list = ['a', 'b', 'c', 'd', 'e', 'f']
my_str = "".join(my_list[::2])
print(my_str)

#######################

my_string_1 = "21"
my_string_2 = "34"
for symb_1 in my_string_1:
    for symb_2 in my_string_2:
        print(symb_1 + symb_2)

#Результат:
"13"	# перебирается все элементы из my_string_2 для элемента "1" из my_string_1
"14"
"23"	# перебирается все элементы из my_string_2 для элемента "2" из my_string_1
"24"
#####################################################