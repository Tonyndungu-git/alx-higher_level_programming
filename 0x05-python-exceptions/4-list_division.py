#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    shorter_length = min(len(my_list_1), len(my_list_2), list_length)

    for i in range(shorter_length):
        try:
            if not isinstance(my_list_1[i], int) or not isinstance(my_list_2[i], int):
                raise TypeError("wrong type")
            if my_list_2[i] == 0:
                raise ZeroDivisionError("division by 0")
            result.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError as e:
            print(e)
            result.append(0)
        except TypeError as e:
            print(e)
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass

    # Add zeros for remaining elements in longer list(s)
    result += [0] * (list_length - shorter_length)

    return result

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
