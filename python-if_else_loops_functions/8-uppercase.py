#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for char in str:
        if 'a' <= char <= 'z':
            upper_str += chr(ord(char) - 32)
        else:
            upper_str += char
    print(upper_str)
