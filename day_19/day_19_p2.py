import sys
from collections import defaultdict,deque
import heapq

def count(ranges,name = 'in'):
    if name == 'R':
        return 0
    if name == 'A':
        prod = 1
        for lo,hi in ranges.values():
            prod *= hi-lo + 1
        return prod
    
    rules = flow_map[name][:-1]
    default = flow_map[name][-1]

    res = 0
    
    for j in rules:
        iii = j.find(':')
        comp = j[0]
        op = j[1]
        n = int(j[2:iii])
        dest = j[iii+1:]
        lo,hi = ranges[comp]
        
        if op == '<':
            T = (lo, min(n - 1, hi))
            F = (max(n, lo), hi)
        else:
            T = (max(n + 1, lo), hi)
            F = (lo, min(n, hi))
            
        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[comp] = T
            res += count(copy, dest)
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[comp] = F
        else:
            break
        
    else:
        res += count(ranges,default)
    
    return res
        
    
if __name__ == "__main__":
    
    inputs = sys.stdin.read().splitlines()
    #print(inputs)
    idx = inputs.index("")
    
    flow = inputs[:idx]
    objs = inputs[idx+1:]
    
    # print(flow)
    # print(objs)
    
    flow_map = {}
    
    for f in flow:
        idx = f.find('{')
        flow_map[f[:idx]] = f[idx+1:-1].split(',')
    
    #print(flow_map)
    
    print(count({key:(1,4000) for key in "xmas"}))
    
    
    
    
