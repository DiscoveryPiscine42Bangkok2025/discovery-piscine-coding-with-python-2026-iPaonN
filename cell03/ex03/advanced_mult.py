#!/usr/bin/env python3

x, y, z = 0, 0, 0

while x <= 10:
    print(f"Table de {x}: ", end="")
    while y <= y*x:
        print(y, end=" ")
        y+= x
        if z == 10:
            print("")
            break
        z+=1
    x+=1
    y = 0
    z = 0
