#!/usr/bin/env python3

import sys

an_array = sys.argv

if len(an_array) -1 >= 1:
    in_str = str(input("What was the parameter? "))
    if in_str == an_array[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")
