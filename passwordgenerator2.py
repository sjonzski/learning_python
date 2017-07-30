#!/usr/bin/env python3

import random
for i in range(1,101):
    password = '' 

    f = open("/Users/shinzietandun/Desktop/parts of speech word files/adjectives/1syllableadjectives.txt","r")
    lines = f.readlines()
    length = len(lines)
    r = random.randint(0,length-1)
    password = password + lines[r][0:-1].title()

    f = open("/Users/shinzietandun/Desktop/parts of speech word files/adjectives/2syllableadjectives.txt","r")
    lines = f.readlines()
    length = len(lines)
    r = random.randint(0,length-1)
    password = password + lines[r][0:-1].title()

    f = open("/Users/shinzietandun/Desktop/parts of speech word files/nouns/3syllablenouns.txt","r")
    lines = f.readlines()
    length = len(lines)
    r = random.randint(0,length-1)
    password = password + lines[r][0:-1].title()

    r = str(random.randint(10,99))
    password = password + r

    print(password)
