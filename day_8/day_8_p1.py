import sys
from collections import defaultdict

if __name__ == "__main__":
    inputs = sys.stdin.read().splitlines()
    
    LR = inputs[0]
    n = len(LR)
    g = [i.split('=') for i in inputs[2:]]
    
    graph = defaultdict(lambda:"")
    
    for i in g:
        graph[i[0].strip(" ")] = i[1][2:-1].split(", ")
    
    #print(graph)

    curr = 'AAA'
    #print(graph[curr])
    
    res = 0
    idx = 0
    while(curr != 'ZZZ'):
        d = LR[idx]
        if d == 'L':
            curr = graph[curr][0]
        else:
            curr = graph[curr][1]
        idx+=1
        res+=1
        if idx >= n:
            idx = idx%n
        
    print(res)
