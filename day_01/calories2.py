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
    elf_cals.sort(key=lambda x : -x)
    print('Top three elf calories:', sum(elf_cals[:3]))

if __name__ == '__main__':
    main()
