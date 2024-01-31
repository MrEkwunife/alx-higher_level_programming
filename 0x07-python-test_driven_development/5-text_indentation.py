#!/usr/bin/python3

"""function defination below"""

def text_indentation(text):
    """This prints a text with 2 new lines
    after each of these characters: `.`, `?` and `:`
    Args:
        text (str)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.split(" ")
    for i in range(len(text)):
        if text[i][-1] in [".", "?", ":"]:
            print(text[i])
            print()
        else:
            if i == len(text) - 1:
                print(text[i], end="")
            else:
                print(text[i], end=" ")
