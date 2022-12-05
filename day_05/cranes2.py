#!/bin/env python3

import sys

def main():
    
    lines = sys.stdin.readlines()
    
    stack_lines = []
    instructions = []
    
    parsed_stacks = False
    for line in lines:

        # parse lines describing stacks:
        if not parsed_stacks:
            if len(line.strip()) == 0:
                parsed_stacks = True
                continue
            stack_lines.append(line)
        else: # parse instructions:
            tokens = line.strip().split()
            assert(tokens[0] == 'move')
            assert(tokens[2] == 'from')
            assert(tokens[4] == 'to')
            instructions.append(
                (int(tokens[1]), int(tokens[3]), int(tokens[5])))

    # further parse stack lines:
    col_line = stack_lines[-1]
    col_names = col_line.split()
    col_idxs = [ col_line.index(s) for s in col_names ]
    stacks = { int(s) : [] for s in col_names }
    for sl in reversed(stack_lines[:-1]):
        for n, i in zip(col_names, col_idxs):
            if i < len(sl) and sl[i] != ' ':
                stacks[int(n)].append(sl[i])
    
    for n, src, tgt in instructions:
            moved = stacks[src][-n:]
            stacks[src] = stacks[src][:-n]
            stacks[tgt] += moved

    print(stacks)    
    msg = ''.join([ stacks[int(n)][-1] for n in col_names]) 
    print('Message: ', msg)

if __name__ == '__main__':
    main()
            
