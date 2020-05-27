#!/usr/bin/env python3

#
# bitfield manipulation
#

# bfd session key(bigdian): 0000F95C

import json

def get_interval_val(value, low , upper):
    interval = upper - low
    dst = value >> low
    modulo = (1 << (interval + 1)) - 1

    return dst & modulo


class bf(object):
    def __init__(self, value=0):
        self._d = value

    def __getitem__(self, key):

        return self._d[key]

def main():
    fpt = open("configure.json")
    js = json.load(fpt)
    configure = bf(js)

    keys_str = input("Input Table Data:")

    numbers = len(keys_str) // 8

    for ind in range(numbers):
        keys = int("0x" + keys_str[ind: ind + 8], base=16)
        print(keys)

        for key, value in configure[ind].items():
            print_val = get_interval_val(keys, value[0], value[1])
            print(key + " :" + str(print_val))


if __name__ == "__main__":
    main()
