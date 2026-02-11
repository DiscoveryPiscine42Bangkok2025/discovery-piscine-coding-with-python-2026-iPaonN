#!/usr/bin/env python3

an_array = [2, 8, 9, 48, 8, 22, -22, 2]
new_array = []

for i in range (len(an_array)):
    if an_array[i] > 5:
        new_array.append(an_array[i] + 2)

new_array = set(new_array)

print(f"{an_array}")
print(f"{new_array}")
