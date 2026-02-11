#!/usr/bin/env python3

import sys

an_array = sys.argv
contain = []

if len(an_array) - 1 >= 1:
    if an_array[1] < an_array[2]:
        i, j = int(an_array[1]), int(an_array[2])
        for i in range(int(an_array[1]), j):
            contain.append(i)
        contain.append(j)
        print(contain)
    else:
        print("none")
else:
    print("none")
