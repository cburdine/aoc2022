#!/bin/env python3

import sys
from pprint import pprint

def main():
   
    _id = None
    items = []
    op = lambda x : 0
    divisor = 0
    true_tgt = -1
    false_tgt = -1
    
    monkeys = {}
    lines = sys.stdin.readlines()
    lines.append('\n')

    for line in lines:
        toks = line.strip().split()
        if len(toks) <= 0:
            if _id not in monkeys:
                monkeys[_id] = { 
                    'items': items,
                    'op' : op,
                    'd': divisor,
                    'tt': true_tgt,
                    'ft': false_tgt,
                }
        elif toks[0].strip() == 'Monkey':
            _id = int(toks[1].strip(':'))
        elif toks[0].strip() == 'Starting':
            items = [ int(t.strip(',')) for t in toks[2:] ]
        elif toks[0].strip() == 'Operation:':
            op = eval('lambda old : ' + ' '.join(toks[3:]))
        elif toks[0].strip() == 'Test:':
            divisor = int(toks[-1])
        elif toks[0].strip() == 'If':
            if toks[1].strip() == 'true:':
                true_tgt = int(toks[-1].strip())
            elif toks[1].strip() == 'false:':
                false_tgt = int(toks[-1].strip())
            else:
                print('Err (If statement): ', toks)
                assert(False)
        else:
            print('Err: ', toks)
            assert(False)

    counts = { i : 0 for i in monkeys.keys() }

    mod_base = 1
    for m in monkeys.values():
        mod_base *= m['d']
    print('using mod base: ', mod_base)
    
    for n in range(10000):
        for _id, m in monkeys.items():
            while m['items']:
                i = m['items'].pop(0)
                ni = m['op'](i) % mod_base
                tgt = m['tt'] if ni % m['d'] == 0 else m['ft']
                counts[_id] += 1
                #print(_id, ':', i, '-', ni, '=>', tgt)
                monkeys[tgt]['items'].append(ni)
        
        #print('-----', n+1, '-----')
        #for _id, m in monkeys.items():
        #    print(_id, ':', m['items'])
    
    top_counts = sorted(counts.values())
    print('counts: ', top_counts)
    print('product: ', top_counts[-1] * top_counts[-2]) 

if __name__ == '__main__':
    main()
