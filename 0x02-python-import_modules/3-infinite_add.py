#!/usr/bin/python3
import sys
j = 0
k = 0
if __name__ == '__main__':
    for i in sys.argv:
        if j == 0:
            j += 1
            continue
        k += int(sys.argv[j])
        j += 1
    print("{}".format(k))
