#!/bin/env python3

import sys

CYCLES = [ 20 + 40*k for k in range(6) ]

def main():
    lines = sys.stdin.readlines()

    x_vals = [1]
    for l in lines:
        toks = l.split()
        instr = toks[0]
        x = x_vals[-1]
        if instr == 'addx':
            n = int(toks[1].strip())
            x_vals.extend([x,x+n])
        elif instr == 'noop':
            x_vals.append(x)
        else:
            assert(False)


    signals = [ x_vals[c-1]*c for c in CYCLES]
    pixels = [ 
        '#' if abs(x_vals[c-1] - (c-1)%40) <= 1  else '.'
        for c in range(1,241)
    ]

    screen = '\n'.join([
        ''.join(pixels[40*k:40*(k+1)]) for k in range(6)
    ])

    print(screen)
    

if __name__ == '__main__':
    main()
