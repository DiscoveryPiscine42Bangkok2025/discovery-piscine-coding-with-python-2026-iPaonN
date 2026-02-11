#!/usr/bin/env python3

import sys

an_array = sys.argv

def shrink(text):
    text = text[0:8]
    return text

def enlarge(text):
    return text + ("Z"*(8 - len(text)))

if len(an_array) - 1 >= 1:
    for i in range(1, len(an_array)):
        if len(an_array[i]) > 8:
            print(shrink(an_array[i]))
        else:
            print(enlarge(an_array[i]))
else:
    print("none")
