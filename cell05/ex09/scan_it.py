#!/usr/bin/env python3

import sys

an_array = sys.argv
count = 0

if len(an_array) -1 >= 2:
    for x in range(2, len(an_array)):
        print(f"{an_array[2].count(an_array[1])}\n")
else:
    print("none")
