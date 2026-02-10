#!/usr/bin/env python3

int_age = int(input("Please tell me your age: "))
start_years = 10

print(f"You are currently {int_age} years old.")

for x in range(3):
    print(f"In {start_years} years, you'll be {int_age} years old.")    
    start_years+=10
    int_age+=10
