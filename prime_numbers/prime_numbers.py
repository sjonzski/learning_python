#!/usr/bin/env python3

i = 3   

while i <= 100:
    for k in range(2,i):
        if i % k == 0:
            break
    else:
        print(i)
    i = i + 1
