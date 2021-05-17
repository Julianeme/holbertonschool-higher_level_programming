#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
        except(ValueError, TypeError):
            count -= 1
            pass
        except (IndexError):
            break
        i += 1
        count += 1
    print()
    return(count)
