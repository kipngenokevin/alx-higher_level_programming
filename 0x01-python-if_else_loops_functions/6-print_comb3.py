#!/usr/bin/python3
for i in range(9):
    for n in range(i + 1, 10):
        if i == 8:
            print("{}{}".format(i, n), end="")
        else:
            print("{}{}".format(i, n), end=", ")
print()
