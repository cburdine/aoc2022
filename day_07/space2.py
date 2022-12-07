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
        

HD_SIZE = 70000000
OS_SIZE = 30000000

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
    needed_size = OS_SIZE - (HD_SIZE - total)
    smallest_size = min(s for s in sizes if s >= needed_size)
    print('smallest size: ', smallest_size)

if __name__ == '__main__':
    main()    
