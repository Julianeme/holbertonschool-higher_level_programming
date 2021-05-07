#!/usr/bin/python3
def roman_to_int(roman_string):
    r_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    j = 1
    i = 0
    if len(roman_string) == 1:
        return(r_num[roman_string[i]])
    for i in range(0, len(roman_string)):
        if roman_string[j] and r_num[roman_string[i]] < r_num[roman_string[j]]:
            total = total + r_num[roman_string[j]] - r_num[roman_string[i]]
            j = j + 1
            if j < len(roman_string):
                i = i + 2
                j = i + 1
            else:
                return total
        else:
            total = total + r_num[roman_string[i]]
            j = i + 1
    return(total)
