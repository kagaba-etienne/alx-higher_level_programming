#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            if (i == x - 1):
                print("")
        return x
    except IndexError:
        print("")
        return i
    except TypeError:
        return i
