#!/bin/env python3

import sys
from pprint import pprint

def dir_sizes(d, l=[]):
    total = 0
    for k, v in d.items():
        if isinstance(v,int):
            total += v
        else:
            total += dir_sizes(v,l)
        
    l.append(total)
    return total
        

def main():
    fs = {}
    path = [fs]
    lines = sys.stdin.readlines()
    for line in lines:
        toks = line.strip().split()
        
        # parse command:
        if toks[0] == '$':
            if toks[1] == 'cd':
                if toks[2] == '..':
                    path.pop()
                else:
                    if toks[2] not in path[-1]:
                        path[-1][toks[2]] = {}
                    path.append(path[-1][toks[2]])
                
            elif toks[1] == 'ls':
                continue                
        
        elif toks[0] == 'dir': # parse dir  entry:
            if toks[1] not in path[-1]:
                path[-1][toks[1]] = {}
        
        else: # parse file entry:
            path[-1][toks[1]] = int(toks[0])
        
    #pprint(fs)
    
    # compute directory sizes:
    sizes = []
    total = dir_sizes(fs, sizes)
    small_sum = sum([ s for s in sizes if s <= 100000 ])    
    print('sum: ', small_sum)

if __name__ == '__main__':
    main()    
