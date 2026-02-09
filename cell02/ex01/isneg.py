#!/usr/bin/env python3

int_input = int(input())

if int_input == 0:
    print("This number is both positive and negative.")
elif int_input < 0:
    print("This number is negative.")
else:
    print("This number is positve.")
