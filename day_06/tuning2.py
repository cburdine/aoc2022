#!/bin/env python3

import sys

def main():
    line = sys.stdin.readlines()[0].strip()
    for i in range(len(line)-14):
        if len(set(line[i:i+14])) >= 14:
            print('packet index: ', i+14)
            break
        


if __name__ == '__main__':
    main()
