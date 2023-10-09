#!/usr/bin/python3
def print_alphabet(char=65): print("{}".format(chr(char)), end=""), char != 90 and print_alphabet(char + 1)
print_alphabet(), print()
