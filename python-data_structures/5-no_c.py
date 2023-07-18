#!/usr/bin/python3
#5-no_c.py


def no_c(my_string):
    result = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            result += char
    return result

