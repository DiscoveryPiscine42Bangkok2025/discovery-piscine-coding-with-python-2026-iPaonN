#!/usr/bin/env python3

an_array = [2, 8, 9, 48, 8, 22, -22, 2]
new_array = []

for i in range (len(an_array)):
    new_array.append(an_array[i] + 2)

print(f"Original array: {an_array}")
print(f"New array: {new_array}")
