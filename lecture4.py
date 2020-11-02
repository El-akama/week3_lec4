# try except внизу
# list comprehension

# nums = [x for x in range(1,11)]
# print(nums)

# nums = []
# for x in range(1,11):
#     nums.append(x)
# print(nums)

# nums = [x for x in range(1,11) if x % 2 == 0]
# nums = [x for x in range(2,11,2)]
# print(nums)


# nums = [1, 9, 3, -4, 15, -6, 0, -1, 5, 8, 33]
# positive = [num for num in nums if num >= 0]
# odd_nums = [num for num in nums if num % 2 != 0 or num < 0]
# fil = [num // 3 if num % 3 == 0 else 0 for num in nums if num > 0]
# print(odd_nums)
# print(fil)

#--------------------------------

# dict comprehension

# sodi = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
# sodi['f'] = 4
# nedi = {}
# for key, value in sodi.items():
#     # print(key)
#     # print(value)
#     nedi[value] = key
# print(nedi)
# for x in sodi.values():
#     print(x)

# dict_ = {value * 2: key if value == 1 else key for key, 
#         value in sodi.items() if value % 2}
# print(dict_)

# -----------------------------------------

# set comprehension

# setso = {'aijana', 'larisa', 'bakyt', 'anton'}
# setne = {name.capitalize() for name in setso if name.startswith('a')}      # startswith('a') метод ищет по начальной букве
# print(setne)

# ----------------------
# [1, 2, 3, 4, 5, 6, 7, 8, 9] должно получится так

# lust = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# nelust = []
# for item in lust:
#     for i in item:
#         nelust.append(i)

# print(nelust)

#---------------------------------------

# try except лекцтя 3_4

# number_a = int(input())
# number_b = int(input())
# result = None
# try:
#     result = number_b / number_a
#     print(result)
# except ZeroDivisionError:
#     result = 0
# finally:
#     print('Калькулятор закончил работу')

# flag = True
# while flag:
#     num1 = 6
#     num2 = input("enter number: ")
    # try:
    #     num2 = int(num2)
    # except ValueError:
    #     print('incorrect')
    #     continue
    # try:
    #     res = num1 / num2
    #     print(res)
    #     # flag = False                          # можно так но если в начале есть флаг трушный
    #     break                                   # и так можно без разницы полюбому остановит
    # except ZeroDivisionError:
    #     print('zero has not found')
    #     continue
    
    # finally:
    #     print('end')

    # try:
    #     num2 = int(num2)
    #     res = num1 / num2
    #     print(res)
    #     break
    # except ValueError:
    #     print('incorrect')
    #     continue
    # except ZeroDivisionError:
    #     print('zero has not found')
    #     continue
    
# ---------------


# num1 = 6
# num2 = 0
# try:
#     res = num1 / num2
#     print(res)
# except ZeroDivisionError:
#     print('zero has not found')
# else:                                           # работает только когда try сработало
#      print('not error')
# finally:                                        # работает всегда
#     print('good job')
        


# num1 = 6
# num2 = 0
# try:
#     res = num1 / num2
#     print(res)
# except ZeroDivisionError:
#     raise Exception('zero has not found')           # вызвает свою ошибку
# else:
#      print('not error')
# finally:
#     print('good job')
