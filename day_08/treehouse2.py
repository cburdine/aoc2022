#!/bin/env python3

import sys

from itertools import product

def main():
    lines = sys.stdin.readlines()
    trees = [ [int(ch) for ch in l.strip() ] for l in lines ]    
    rows, cols = len(trees), len(trees[0])
    view_scores =  [ [ None for _ in range(cols) ] for _ in range(rows) ]
     

    for i in range(rows):
        for j in range(cols):
            h = trees[i][j]
            vds = [0, 0, 0, 0]
            
            for di in range(i+1, rows):
                vds[0] += 1
                if trees[di][j] >= h:
                    break

            for di in reversed(range(0,i)):
                vds[1] += 1
                if trees[di][j] >= h:
                    break
            
            for dj in range(j+1, cols):
                vds[2] += 1
                if trees[i][dj] >= h:
                    break
                
            for dj in reversed(range(0, j)):
                vds[3] += 1
                if trees[i][dj] >= h:
                    break

            view_scores[i][j] = vds[0] * vds[1] * vds[2] * vds[3]

    best_score = max( max(v) for v in view_scores )
    print('best scenic score: ', best_score)

    


if __name__ == '__main__':
    main()
