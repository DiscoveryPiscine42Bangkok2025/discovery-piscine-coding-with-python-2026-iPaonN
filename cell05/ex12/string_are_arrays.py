#!/usr/bin/env python3

import sys

an_array = sys.argv

if len(an_array) - 1 >= 1:
    if an_array[1].count("z") > 0:
        print("z" * an_array[1].count("z"))
    else:
        print("none")
else:
    print("none")
