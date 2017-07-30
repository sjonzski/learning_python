#!/usr/bin/env python3

print("How far to count?")
howfar = int(input())

while howfar < 1:
    print("Not a valid number, pls try again")
    howfar = int(input())

for i in range(1, howfar):
    if i % 3 == 0 and i % 5 == 0:
        print("fizz buzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
