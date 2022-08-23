#!/usr/bin/python3

def remove_char_at(str, n):
    if len(str) > n:
        if not n < 0:
            str = str[:n] + str[n + 1:]
    print(str)
