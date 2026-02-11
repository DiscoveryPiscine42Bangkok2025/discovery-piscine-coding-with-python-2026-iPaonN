#!/usr/bin/env python3

in_num = float(input("Give me a number: "))

if str(in_num).isdigit():
    print("This number is an integer.")
else:
    print("This number is a decimal.")
