#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for n in range(list_length):
        try:
            result_div = my_list_1[n] / my_list_2[n]
        except TypeError:
            print("wrong type")
            result_div = 0
        except ZeroDivisionError:
            print("division by 0")
            result_div = 0
        except IndexError:
            print("out of range")
            result_div = 0
        finally:
            result.append(result_div)
    return result
