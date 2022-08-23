#!/usr/bin/python3
for i in range(8):
    for j in range(i+1, 10):
        print(f"{0:d}{1:d}".format(i, j), end=', ')
print("{:d}".format(89))
