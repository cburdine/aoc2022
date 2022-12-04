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
    lines = sys.stdin.readlines()
    for i in range(len(lines)//3):
        group = [ set(l.strip()) for l in lines[3*i:3*(i+1)] ]
        
        items = list(group[0] & group[1] & group[2])
        assert(len(items) == 1)
        total += priority(items[0])

    print('Total: ', total)

if __name__ == '__main__':
    main()
        
