#!/usr/bin/python3
for i in range(9):
    for j in range(1,10):
        if(i==8 and j==9):
            print(f"{i}{j}")
        else:
            print("{:d}{:d}".format(i,j), end=" ")