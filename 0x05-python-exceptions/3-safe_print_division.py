#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        val = a / b
    except zeroDivisionError:
        val = None
    finally:
        print("Inside result {:d}".format(val))
    return val
