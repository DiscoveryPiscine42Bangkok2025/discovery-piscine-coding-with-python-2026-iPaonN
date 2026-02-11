#!/usr/bin/env python3

import sys

an_array = sys.argv

if len(an_array) - 1 >= 1:
    for i in range(1, len(an_array)):
        if an_array[i].find("ism") == -1:
            an_array[i]+="ism"
            print(an_array[i])
        else:
            continue
else:
    print("none")
