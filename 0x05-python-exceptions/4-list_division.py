#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n = 0
    result = []
    while n < list_length:
        try:
            division = my_list_1[n] / my_list_2[n]
        except (TypeError, ValueError):
            division = 0
            print("wrong type")
        except ZeroDivisionError:
            division = 0
            print("division by 0")
        except IndexError:
            division = 0
            print("out of range")
        finally:
            result.append(division)
            n += 1
    return result
