#!/bin/env python3

import sys

def main():
    line = sys.stdin.readlines()[0].strip()
    for i in range(len(line)-4):
        if len(set(line[i:i+4])) >= 4:
            print('packet index: ', i+4)
            break
        


if __name__ == '__main__':
    main()
