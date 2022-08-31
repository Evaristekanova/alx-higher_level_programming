#!/usr/bin/python3
def value(r):
    if(r == "I"):
        return 1
    if(r == "V"):
        return 5
    if(r == "X"):
        return 10
    if(r == "L"):
        return 50
    if(r == "C"):
        return 100
    if(r == "D"):
        return 500
    if(r == "M"):
        return 1000
    return -1

def roman_to_int(rom_str):
    result = 0
    idx = 0
    leng = len(rom_str)
    while(idx < len(rom_str)):
        f = value(rom_str[idx])
        if(idx + 1 < len(rom_str)):
            f2 = value(rom_str[idx + 1])
            if(f >= f2):
                result += f
                idx += 1
            else:
                result += f2 - f
                idx += 2
        else:
            result += f
            idx += 1
    return result
