#!/usr/bin/python3
def uppercase(str):
    chars = []

    for char in str:
        if 97 <= ord(char) <= 122:
            chars.append(chr(ord(char) - 32))
        else:
            chars.append(char)
    print("{}".format("".join(chars)))
