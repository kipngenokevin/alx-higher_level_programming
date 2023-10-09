#!/usr/bin/python3
import sys
if __name__ == "__main__":
    j = 0
    total_arguments = len(sys.argv)
    if total_arguments == 1:
        print("{} arguments.".format(total_arguments - 1))
    elif total_arguments == 2:
        print("{} argument:".format(total_arguments - 1))
    else:
        print("{} arguments:".format(total_arguments - 1))
    for i in sys.argv:
        if j == 0:
            j += 1
            continue
        print("{}: {}".format(j, sys.argv[j]))
        j += 1
