#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        for val, index in enumerate(my_list, start=1):
            if index == idx:
                my_list[idx] = element
        return my_list
    else:
        return my_list
