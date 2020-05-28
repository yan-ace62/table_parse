  #
# bitfield manipulation
#

# bfd session key(bigdian): 0000F95C
# bfd session result: 00000011 00000000
# key + result: 0000F95C0000001100000000

#!/usr/bin/env python3

import json
import argparse

def load_configure():
    files = open("configure.json")
    config_data = json.load(files)
    return config_data

def make_argparse():
    parser = argparse.ArgumentParser(description='Parse np table.')
    parser.add_argument('--key', action='store_true', help='Parse np key.')
    parser.add_argument('--result', action='store_true', help='Parse np result.')
    parser.add_argument('--n', action='store', metavar='number', help='the position of parsing.')

    return parser

class bf(object):
    def __init__(self, value=0):
        self._d = value

    def __getitem__(self, key):

        return self._d[key]

    def key(self):
        return self._d["key"]

    def result(self):
        return self._d["result"]

def get_interval_val(value, low , upper):
    interval = upper - low
    dst = value >> low
    modulo = (1 << (interval + 1)) - 1

    return dst & modulo

def do_parse_key(int_list, key_config):
    loop_number = min(len(int_list), len(key_config))
    key_obj = {}

    for ind in range(loop_number):
        keys = int_list[ind]

        for key, value in key_config[ind].items():
            value = get_interval_val(keys, value[0], value[1])
            key_obj[key] = value

    return key_obj
             

def do_parse_result(int_list, result_configure):
    loop_number = min(len(int_list), len(result_configure))

    for ind in range(loop_number):
        keys = int_list[ind]

        for key, value in result_configure[ind].items():
            print(key)
            print(":")
            print(get_interval_val(keys, value[0], value[1]))

def do_parse_table(argument, int_list, configure):
    if argument['key'] & argument["result"]:
        return False
    elif argument['key']:
        key_obj = do_parse_key(int_list, configure["key"])
        print(key_obj)
    elif argument["result"]:
        do_parse_result(int_list, configure["result"])
    else:
        do_parse_key(int_list, configure["key"])
        if len(int_list) > len(configure["key"]):
            int_list = int_list[len(configure["key"]):]
            do_parse_result(int_list, configure["result"])

def do_parse_input_data(str_data):
    numbers = len(str_data) // 8
    int_list = []
    for ind in range(numbers):
        int_list.append(int(str_data[ind: ind+8], base=16))

    return int_list

def main():
    config_data = load_configure()
    configure = bf(config_data)

    parser = make_argparse()

    argument = parser.parse_args()

    argument = vars(argument)

    #print(type(vars(argument)))
    #print(vars(argument))

    #print(configure.key())
    #print(configure.result())
    #print(configure["key"])

    table_data = input("Input Table Data:")

    int_list = do_parse_input_data(table_data)
    print(int_list)
    do_parse_table(argument, int_list, configure)


if __name__ == "__main__":
    main()
