#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return (0)

    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i, s in enumerate(roman_string):
        if (i < len(roman_string) - 1 and
                r_dict[s] < r_dict[roman_string[i + 1]]):
            total -= r_dict[s]
        else:
            total += r_dict[s]
    return total
