#!/usr/bin/env python3

in_num = input("Give me a number: ")

if str(in_num).isdigit():
    print("This number is an integer.")
#elif str(in_num).isdecimal():
else:
    print("This number is a decimal.")
