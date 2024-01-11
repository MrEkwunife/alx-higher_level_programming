#!/usr/bin/python3

'''
def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_string = roman_string.upper()
    roman_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0

    prev = roman_values[roman_number[0]]

    for i in roman_string:
        if i in list(roman_values.keys()):
            total += roman_values[i]
            if prev < roman_values[i]:
                total -= prev * 2
            prev = roman_values[i]
        else:
            return 0
    return total
'''


def subract_(list_):
    to_sub = 0
    max_ = max(list_)

    for n in list_:
        if max_ > n:
            to_sub += n

    return (max_ - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    list_keys = list(rom_n.keys())

    num = 0
    last_rom = 0
    list_num = [0]

    for i in roman_string:
        for r_num in list_keys:
            if r_num == i:
                if rom_n.get(i) <= last_rom:
                    num += subract_(list_num)
                    list_num = [rom_n.get(i)]
                else:
                    list_num.append(rom_n.get(i))

                last_rom = rom_n.get(i)

    num += subract_(list_num)

    return (num)
