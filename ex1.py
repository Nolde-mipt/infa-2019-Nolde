#!/user/bin/env python3
def simple_number_add(list_name, max_number):
    r"""принимает на вход list list_name и натуральное число max_number\
            добавляет в list_name все простые числа, не превышающие max_number"""
    if max_number > 0 and int(max_number) == max_number:
        for i in range(2, max_number):
            flag = True
            for p in range(1, len(list_name)):
                if i % list_name[p] == 0: #'деление на 1 не произвожится, т. к. 1 является нулевым элементом массива'
                    flag = False
            if flag:
                list_name.append(i)

simple_number_list = [1]
upper_edge = (int(input()))
simple_number_add(simple_number_list, upper_edge)
print(simple_number_list)
