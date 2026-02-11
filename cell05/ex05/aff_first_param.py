#!/usr/bin/env python3

import sys

an_array = sys.argv

if len(an_array) < 2:
    print("none")
else:
    print(f"{(an_array)[1]}\n")
