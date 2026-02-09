#!/usr/bin/env python3

in_one = int(input("Enter the first number:\n"))
two_in = int(input("Enter the second number:\n"))

result = in_one * two_in

print(f"{in_one} x {two_in} = {result}")
print(f"The result is ", end="")

if result == 0:
    print("positive and negative.")
elif result > 0:
    print("positive.")
else:
    print("negative.")
