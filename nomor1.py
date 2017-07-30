#!/usr/bin/env python3

def get_num():
    num = int(input())
    return num

def convert_to_binary(decimal):
    arr = []
    while decimal > 0:
        remainder = decimal % 2
        arr.append(remainder)
        decimal = int(decimal / 2)
    return arr

def main():
    num = get_num()
    binary = convert_to_binary(num)
    binary.reverse()
    print(binary)

main()
