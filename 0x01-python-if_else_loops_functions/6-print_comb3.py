#!/usr/bin/python3
for i in range(9):
    for j in range(i+1, 10):
        if i == 8:
            print("{0:d}{1:d}".format(i, j))
            break
        print("{0:d}{1:d}".format(i, j), end=', ')
