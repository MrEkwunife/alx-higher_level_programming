#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
out = "Last digit of {} is {} and is {}"
last_dg = abs(number + (abs(number) % 10)) - abs(number)

if last_dg > 5:
    print(out.format(number, last_dg, "greater than 5"))
elif last_dg == 0:
    print(out.format(number, last_dg, "0"))
else:
    print(out.format(number, last_dg, "less than 6 and not 0"))
