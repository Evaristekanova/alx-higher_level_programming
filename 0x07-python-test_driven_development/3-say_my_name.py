#!/usr/bin/python3
'''
module: say_my_name
'''
def say_my_name(first_name, last_name=""):
    """
    printing first name and last name
    first_name --- string
    last_name --- string
    """
    # ERROR MESSAGE DICT #
    err_msg = {}
    err_msg["first_name"] = "first name must be a string"
    err_msg["last_name"] = "last name must be a string"

    # TEST #

    if type(first_name) != str:
        raise TypeError (err_msg["first_name"])
    if type(last_name) != str:
        raise TypeError (err_msg["last_name"])
    print("My name is {}".format(first_name))
    if len(last_name) == 0:
        print("")
    else:
    print(" {}".format(last_name))
