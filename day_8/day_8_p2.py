import sys
from collections import defaultdict
from math import gcd

if __name__ == "__main__":
    inputs = sys.stdin.read().splitlines()
    
    LR = inputs[0]
    n = len(LR)
    g = [i.split('=') for i in inputs[2:]]
    
    graph = defaultdict(lambda:"")
    
    for i in g:
        graph[i[0].strip(" ")] = i[1][2:-1].split(", ")
    
    #print(graph)

    curr = []
    for i in graph.keys():
        if i[-1] == 'A':
            curr.append(i)

    res = []
    
    for start in curr:
        temp = start
        res_temp = 0
        idx = 0
    
        while(temp[-1] != 'Z'):
            d = LR[idx]
            if d == 'L':
                temp = graph[temp][0]
            else:
                temp = graph[temp][1]
            res_temp+=1
            idx += 1
            if idx >= n:
                idx%=n
        
        res.append(res_temp)
    
    res = set(res)
    lcm = 1
    for i in res:
        lcm = (lcm*i)//gcd(lcm, i)
    
    print(lcm)