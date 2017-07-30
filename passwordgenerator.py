#!/usr/bin/env python3

#AQA Computing Topic 3.12
#Password Generator
#04 07 2017

firstname = input("Enter your first name> ")
while not firstname.isalpha():
    firstname = input("Enter your first name> ")
    
secondname = input("Enter your second name> ")
while not secondname.isalpha():
    secondname = input("Enter your secondname> ")

y_o_b = input("Enter your year of birth> ")
while not y_o_b.isnumeric() or not len(y_o_b) == 4:
    y_o_b = input("Enter your year of birth> ")

favcolor = input("Pick your favourite colour: Blue, Red, Green> ")
while not (favcolor.lower() == 'blue' or favcolor.lower() == 'red' or favcolor.lower() == 'green'):
    favcolor = input("Pick your favourite colour> Blue, Red, Green")


while not favcolor.isalpha():
    favcolor = input("Enter your favourite colour> ")

street = input("Enter your street name> ")
while not street.isalpha():
    street = input("Enter your street name> ")

shoesize = input("Enter your shoe size> ")
while not shoesize.isnumeric():
    shoesize = input("Enter your shoe size> ")

firstname = firstname[0]
secondname = secondname[0:1]
y_o_b = y_o_b[-2::]
favcolor = favcolor[0:3]
street = street[0:3]

password = firstname + secondname + y_o_b + favcolor + street + shoesize

print("Your password is :  {}".format (password))
