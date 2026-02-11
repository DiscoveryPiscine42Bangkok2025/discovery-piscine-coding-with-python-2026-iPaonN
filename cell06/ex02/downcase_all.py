#!/usr/bin/env python3

import sys

input = sys.argv

def downcase_it(text):
    print(text.lower())

if len(input) - 1 >= 1:
    for i in range(1, len(input)):
        downcase_it(input[i])
else:
    print("none")
