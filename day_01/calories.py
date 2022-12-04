#!/bin/env python3

import sys

def main():
    elf_cals = []
    cals = 0
    for line in sys.stdin.readlines():
        line = line.strip()
        if line:
            cals += int(line)
        else:
            elf_cals.append(cals)
            cals = 0
    
    elf_cals.append(cals)
    print('Max calories: ', max(elf_cals))

if __name__ == '__main__':
    main()
