#!/bin/env python3 

import sys

DIRS = { 'R': (1,0), 'U': (0, 1), 'L': (-1,0), 'D': (0,-1) }
def move(h,t,_dir):
    d = DIRS[_dir]
    new_h = (h[0] + d[0], h[1] + d[1])
    new_t = t
    if max(abs(new_h[0] - new_t[0]),
           abs(new_h[1] - new_t[1])) >= 2:
        new_t = h

    return (new_h, new_t)    

def main():
    h, t = (0,0), (0,0)
    tail_pts = { t }
    for line in  sys.stdin.readlines():
        toks = line.split()
        _dir, dist = toks[0].strip(), int(toks[1].strip())
        for _ in range(dist):
            (h,t) = move(h,t,_dir)
            tail_pts.add(t)

    print('# points visited: ', len(tail_pts))

    
if __name__ == '__main__':
    main()
