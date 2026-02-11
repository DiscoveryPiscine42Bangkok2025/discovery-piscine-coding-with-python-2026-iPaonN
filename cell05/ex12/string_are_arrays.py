#!/usr/bin/env python3

import sys

an_array = sys.argv

if len(an_array) -1 >= 1:
    print("parameters: " + str(len(an_array) - 1))
    for x in range(1, len(an_array)):
        print(f"{an_array[x]}: {len(an_array[x])}")
else:
    print("none")
