#!/bin/env python3

import sys

WIN_PTS = [ 3, 6, 0 ]
def main():
    score = 0
    lines = sys.stdin.readlines()
    for line in lines:
        toks = line.split(' ')
        p1 = int(ord(toks[0][0])-ord('A'))
        p2 = int(ord(toks[1][0])-ord('X'))
        s2 = WIN_PTS[(p2-p1) % 3] + (p2 + 1)
        score += s2

    print('Score:', score) 

if __name__ == '__main__':
    main()        
