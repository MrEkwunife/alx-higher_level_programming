#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -2):
    print("{:c}{:c}".format(i, i - 33), end="")
