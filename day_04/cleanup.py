#!/bin/env python3

import sys

def main():

    lines = sys.stdin.readlines()
    overlaps = 0
    
    for line in lines:
        toks = line.split(',')
        r0 = tuple(map(int, toks[0].strip().split('-')))
        r1 = tuple(map(int, toks[1].strip().split('-')))
        if r0[0] <= r1[0] <= r1[1] <= r0[1] or r1[0] <= r0[0] <= r0[1] <= r1[1]:
            overlaps += 1
   
    print('overlaps: ', overlaps)
    

if __name__ == '__main__':
    main()
        
