#!/usr/bin/python3


def text_indentation(text):
    '''
    Prints the given text with 2 new lines after each of these characters: .?:
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    text = text.replace(". ", ".\n\n")
    text = text.replace("? ", "?\n\n")
    text = text.replace(": ", ":\n\n")

    print(text)
