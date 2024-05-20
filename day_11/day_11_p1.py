import sys
from collections import deque
import numpy as np
    
if __name__ == "__main__":

    grid = sys.stdin.read().splitlines()
    
    temp = []
    for i in range(len(grid)):
        temp.append(list(grid[i]))
    #print(len(grid[0]))
    grid = np.array(temp)
    #grid = np.insert(grid,[0],[['.']*10],axis = 0)
    idx = 0
    
    # for i in grid:
    #     print(i)
    
    while(idx < len(grid)):
        n = len(grid[idx])
        if list(grid[idx]) == ['.']*n:
            grid = np.insert(grid,[idx],[['.']*n],axis = 0)
            #grid.insert(idx,['.']*n)
            idx+=1
        idx += 1
        
    idx = 0
    #print(grid)
    grid = grid.T
    while(idx < len(grid)):
        n = len(grid[idx])
        if list(grid[idx]) == ['.']*n:
            grid = np.insert(grid,[idx],[['.']*n],axis = 0)
            #grid.insert(idx,['.']*n)
            idx+=1
        idx += 1
    grid = grid.T
    
    # for i in grid:
    #     print(i)  
        
    lis = []
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                lis.append((i,j))

    res = 0
    for i in range(len(lis)):
        x,y = lis[i]
        for j in range(i+1,len(lis)):
            newx,newy = lis[j]
            res += abs(newx-x) + abs(newy-y)

    print(res)
    
    

    
    
    
