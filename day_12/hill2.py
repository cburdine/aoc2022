#!/bin/env python3

import sys
from heapq import heappush, heappop
from pprint import pprint

def search(graph, start, end=None):
    D = { start: 0 }
    P = { start: start } 
    Q = [ (0,start) ] 
    
    while Q:
        p, v = heappop(Q)
        if v == end:
            break
        for (nv, d) in graph[v]:
            nd = d + D[v]
            if nv not in D or nd < D[nv]:
                heappush(Q,(nd, nv))
                D[nv] = nd
                P[nv] = v
    
    return D, P

def main():
    terrain = [ list(l.strip()) 
                for l in sys.stdin.readlines() if len(l.strip()) ]
    rows = len(terrain)
    cols = len(terrain[0])
    starts, end = [], None
    graph = {}

    for r in range(rows):
        for c in range(cols):
            ch = terrain[r][c]
            if ch == 'S' or ch == 'a':
                terrain[r][c] = 'a'
                starts.append((r,c))
            elif ch == 'E':
                end = (r,c)
                terrain[r][c] = 'z'

    for r in range(rows):
        for c in range(cols):            
            ch = terrain[r][c]    
            graph[(r,c)] = []
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                r2, c2 = r+dr, c+dc
                if 0 <= r2 < rows and 0 <= c2 < cols:
                    ch2 = terrain[r2][c2]
                    if ord(ch2)-ord(ch) <= 1:
                        graph[(r,c)].append( ((r2,c2),1) )

    start_costs = []
    for start in starts:
        costs, _ = search(graph, start, end)
        if end in costs:
            start_costs.append(costs[end])

    print('minimal distance: ', min(start_costs))

if __name__ == '__main__':
    main()
