#1/usr/bin/python3
def multiply_by_2(a_dictionary):
    for idx, val in sorted(a_dictionary.items()):
        print("{} : {}".format(idx, val * 2))
