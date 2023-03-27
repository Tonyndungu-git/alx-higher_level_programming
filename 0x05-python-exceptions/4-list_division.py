#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list = []
    count = 0

    for i in range(list_length):
        try:
            if isinstance(my_list_1[i], int) and isinstance(my_list_2[i], int):
                try:
                    list.append(my_list_1[i] / my_list_2[i])
                except ZeroDivisionError:
                    print("division by 0")
            else:
                raise TypeError
        except IndexError:
            print("out of range")
            break
        except TypeError:
            print("wrong type")
        else:
            count += 1

    return list
