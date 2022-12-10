#!/bin/env python3

import sys

from itertools import product

def main():
    lines = sys.stdin.readlines()
    trees = [ [int(ch) for ch in l.strip() ] for l in lines ]    
    rows, cols = len(trees), len(trees[0])
    vis = [ [0 for _ in range(cols)] for _ in range(rows) ]

    # sweep rows:
    for i in range(rows):
        h = -1
        for j in range(cols):
            if trees[i][j] > h:
                vis[i][j] = 1 
                h = trees[i][j]
        h = -1
        for j in reversed(range(cols)):
            if trees[i][j] > h:
                vis[i][j] = 1 
                h = trees[i][j]
        
    # sweep cols:
    for j in range(cols):
        h = -1
        for i in range(rows):
            if trees[i][j] > h:
                vis[i][j] = 1 
                h = trees[i][j]
        h = -1
        for i in reversed(range(rows)):
            if trees[i][j] > h:
                vis[i][j] = 1 
                h = trees[i][j]
        
    #print('\n'.join([''.join(list(map(str,v))) for v in vis ]))

    total_vis = 0
    for i,j in product(range(rows),range(cols)):
        if vis[i][j]:
            total_vis += 1
    
    print('total visible: ', total_vis)


if __name__ == '__main__':
    main()
