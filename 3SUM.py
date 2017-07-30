#!/usr/bin/env python3
#sjonzski

import itertools
import time

l = '9 -6 -5 9 8 3 -4 8 1 7 -4 9 -9 1 9 -9 9 4 -6 -8'
l = list(map(int, l.split()))

answer = []
for i in range(len(l)):
    for j in range(len(l)):
        if j > i:
            look_for = (-1) * (l[i] + l[j])
            print(l[i], l[j], look_for)
            if look_for in l and (l.index(look_for) > j):
                answer.append([l[i], l[j], look_for])
                print('found!')

for ans in answer:
    ans.sort()

answer.sort()
print(answer)

print(list(answer for answer,_ in itertools.groupby(answer)))
