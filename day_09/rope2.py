#!/bin/env python3 

import sys

DIRS = { 'R': (1,0), 'U': (0, 1), 'L': (-1,0), 'D': (0,-1) }
sgn = lambda x : 1 if x > 0 else -1

def move(rope,_dir):
    d = DIRS[_dir]
    h = list(rope[0])
    rope[0] = (h[0] + d[0], h[1] + d[1])
    for i in range(1,len(rope)):
        h, t = list(rope[i-1]), list(rope[i])
        if abs(h[0] - t[0]) >= 2:
            t[0] += sgn(h[0] - t[0])
            if abs(h[1] - t[1]) >= 1:
                t[1] += sgn(h[1] - t[1])
            
        elif abs(h[1] - t[1]) >= 2:
            t[1] += sgn(h[1] - t[1])
            if abs(h[0] - t[0]) >= 1:
                t[0] += sgn(h[0] - t[0])
        
        rope[i] = tuple(t)

def print_rope(rope, r=20):
    for y in reversed(range(-r,r)):
        line = ''
        for x in range(-r,r):
            if (x,y) in rope:
                line += str(rope.index((x,y)))
            elif (x,y) == (0,0):
                line += 's'
            else:
                line += '.'
        print(line)


def main():
    rope = [ (0,0) for _ in range(10)]
    tail_pts = { rope[-1] }
    for line in  sys.stdin.readlines():
        toks = line.split()
        _dir, dist = toks[0].strip(), int(toks[1].strip())
        for _ in range(dist):
            move(rope,_dir)
            tail_pts.add( rope[-1] )

        
        #print_rope(rope)

    print('# points visited: ', len(tail_pts))

    
if __name__ == '__main__':
    main()
