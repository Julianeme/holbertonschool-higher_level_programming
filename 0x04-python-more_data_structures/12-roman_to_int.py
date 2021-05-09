#!/usr/bin/python3
def roman_to_int(roman_string):
    r_str = roman_string
    r_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0
    if r_str is None or type(r_str) != str:
        return(0)
    if len(r_str) == 1:
        return(r_num[r_str[i]])
    while i < len(r_str):
        j = i + 1
        if j < len(r_str) and r_num[r_str[i]] < r_num[r_str[j]]:
            total = total + r_num[r_str[j]] - r_num[r_str[i]]
            i = i + 1
            if j >= len(r_str) - 1:
                return total
        else:
            total = total + r_num[r_str[i]]
        i += 1
    return(total)
