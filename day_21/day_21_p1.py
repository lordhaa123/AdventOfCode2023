import sys
from collections import defaultdict,deque

    
if __name__ == "__main__":
    
    inputs = sys.stdin.read().splitlines()
    # print(inputs)
    inputs = [[i for i in row] for row in inputs]
    # print(inputs)
    n = len(inputs)
    m = len(inputs[0])
    
    start = [(-1,-1)]
    for i in range(n):
        for j in range(m):
            if inputs[i][j] == 'S':
                start = [(i,j)]
    
    dir = [(-1,0),(0,-1),(1,0),(0,1)]
    steps = 64
    res = 0
    while(steps>0):
        steps -= 1
        lis = []
        for st in start:
            x,y = st
            for dx,dy in dir:
                new_x = x+dx
                new_y = y+dy
                if 0<=new_x<n and 0<=new_y<m and inputs[new_x][new_y] == '.':
                    inputs[new_x][new_y] = 'S'
                    lis.append((new_x,new_y))
        for st in start:
            x,y = st
            inputs[x][y] = '.'
        start = lis
        if steps == 0:
            res += len(start)
    
    
    print(res)
    
    
    
