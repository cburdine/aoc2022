#!/bin/env python3

import sys

def priority(ch):
    if 'a' <= ch <= 'z':
        return ord(ch[0]) - ord('a') + 1
    elif 'A' <= ch <= 'Z':
        return ord(ch[0]) - ord('A') + 27
    else:
        assert(False)

def main():

    total = 0
    for line in sys.stdin.readlines():
        line = line.strip()
        A, B = set(line[:len(line)//2]), set(line[len(line)//2:])
        items = list(A & B)
        assert(len(items) == 1)
        total += priority(items[0])

    print('Total: ', total)

if __name__ == '__main__':
    main()
        
