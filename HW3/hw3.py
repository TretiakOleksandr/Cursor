#1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print('----------1----------')

def printId(x):
    print(id(x))

printId(int_a)
printId(str_b)
printId(set_c)
printId(lst_d)
printId(dict_e)

#2. Append 4 and 5 to the lst_d and define the id one more time.
print('----------2----------')
print(lst_d)
printId(lst_d)
lst_d.append(4)
lst_d.append(5)
print(lst_d)
printId(lst_d)

#3. Define the type of each object from step 1.
print('----------3----------')

def printType(x):
    print(type(x))

printType(int_a)
printType(str_b)
printType(set_c)
printType(lst_d)
printType(dict_e)

#4*. Check the type of the objects by using isinstance.
print('----------4----------')

def typeCheck(x, checkedType):
    print(isinstance(x, checkedType))

typeCheck(int_a, int)
typeCheck(str_b, str)
typeCheck(set_c, set)
typeCheck(lst_d, list)
typeCheck(dict_e, dict)

#String formatting:
#Replace the placeholders with a value:
#"Anna has ___ apples and ___ peaches."

#5. With .format and curly braces {}
print('----------5----------')
print("Anna has {} apples and {} peaches.".format(3, 4))
#6. By passing index numbers into the curly braces.
print('----------6----------')
print("Anna has {1} apples and {0} peaches.".format(3, 4))
#7. By using keyword arguments into the curly braces.
print('----------7----------')
print("Anna has {apple} apples and {peach} peaches.".format(apple = 6, peach = 7))
#8*. With indicators of field size (5 chars for the first and 3 for the second)
print('----------8*----------')
print("Anna has {0:5} apples and {1:3} peaches.".format(234, 78))
#9. With f-strings and variables
print('----------9----------')
apple = 28
peach = 37
print(f"Anna has {apple} apples and {peach} peaches.")
#10. With % operator
print('----------10----------')
apple_num = 18
peach_num = 68
print("Anna has %i apples and %i peaches." % (apple_num, peach_num))
#11*. With variable substitutions by name (hint: by using dict)
print('----------11*----------')
honey_apple_num = 123
pretty_peach_num = 42
fruit_dict = {"first_fruit_num": honey_apple_num, "second_fruit_num": pretty_peach_num}
print("Anna has %(first_fruit_num)i apples and %(second_fruit_num)i peaches." % fruit_dict)


# Comprehensions:
# (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)
#
# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]

# 12. Convert (1) to list comprehension
print('----------12----------')
lst = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst)

# 13. Convert (2) to regular for with if-else
print('----------13----------')
list_comprehension = []
for num in range(10):
    if num % 2 == 0:
        list_comprehension.append(num // 2)
    else:
        list_comprehension.append(num * 10)
print(list_comprehension)

# (3)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
#
# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
#
# (5)
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
#
# (6)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}

#14. Convert (3) to dict comprehension.
print('----------14----------')
d = {num: num ** 2 for num in range(1, 11) if num % 2 == 1 }
print(d)

#15*. Convert (4) to dict comprehension.
print('----------15*----------')
d = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d)

# 16. Convert (5) to regular for with if.
print('----------16----------')
dict_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension[x] = x ** 3
print(dict_comprehension)

#17*. Convert (6) to regular for with if-else.
print('----------17*----------')
dict_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension[x] = x ** 3
    else:
        dict_comprehension[x] = x
print((dict_comprehension))


# Lambda:
#
# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
#
# (8)
# foo = lambda x, y, z: z if y < x and x > z else y

# 18. Convert (7) to lambda function

foo = lambda x, y: x if x < y else y

# 19*. Convert (8) to regular function

def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y




lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# 20. Sort lst_to_sort from min to max
print('----------20----------')
print(sorted(lst_to_sort))

# 21. Sort lst_to_sort from max to min
print('----------21----------')
print(sorted(lst_to_sort, reverse=True))

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print('----------22----------')
print(list(map(lambda x: x * 2, lst_to_sort)))

# 23*. Raise each list number to the corresponding number on another list:
print('----------23*----------')
list_A = [2, 3, 4]
list_B = [5, 6, 7]

#v1
new_list = []
for x in range(len(list_A)):
    new_list.append(list_A[x] ** list_B[x])
print(new_list)

#v2
new_list = [list_A[x] ** list_B[x] for x in range(len(list_A))]
print(new_list)

#v3
print(list(map(lambda x, y: x ** y, list_A, list_B)))

#24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print('----------24----------')
print(list(filter(lambda x: x % 2 == 1, lst_to_sort)))

# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
print('----------25----------')
b = range(-10, 10)
print(list(filter(lambda x: x < 0, list(b))))

# 26*. Using the filter function, find the values that are common to the two lists:
print('----------26*----------')
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
print(list(filter(lambda x: x in list_2, list_1)))
