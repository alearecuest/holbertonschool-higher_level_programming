#!/usr/bin/python3
for numbers in range(0, 10):
    for combinations in range(1, 10):
        if numbers >= combinations:
            continue
        elif numbers == 8 and combinations == 9:
            print("{}{}".format(numbers, combinations))
        else:
            print("{}{}".format(numbers, combinations), end=", ")
