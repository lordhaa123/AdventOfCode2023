import sys
from collections import deque
import numpy as np
    
if __name__ == "__main__":

    grid = sys.stdin.read().splitlines()
    
    temp = []
    for i in range(len(grid)):
        temp.append(list(grid[i]))
    grid = np.array(temp)

    idx = 0
    rows = []
    while(idx < len(grid)):
        n = len(grid[idx])
        if list(grid[idx]) == ['.']*n:
            rows.append(idx)

        idx += 1
        
    idx = 0
    cols = []
    grid = grid.T
    while(idx < len(grid)):
        n = len(grid[idx])
        if list(grid[idx]) == ['.']*n:
            cols.append(idx)
        idx += 1
    grid = grid.T
    
    # print(rows)
    # print(cols)
    
    lis = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == '#':
                lis.append((i,j))
    
    res = 0
    for i in range(len(lis)-1):
        for j in range(i+1,len(lis)):
            
            x_num = 0
            y_num = 0
            for row in rows:
                if row > lis[i][0] and row < lis[j][0]:
                    x_num += 1
                elif row<lis[i][0] and row>lis[j][0]:
                    x_num += 1
            
            for col in cols:
                if col > lis[i][1] and col < lis[j][1]:
                    y_num += 1
                elif col < lis[i][1] and col > lis[j][1]:
                    y_num+=1
            
            res += abs(lis[i][0]-lis[j][0]) + abs(lis[i][1]-lis[j][1])
            res += (1000000-1)*x_num + (1000000-1)*y_num

    print(res)

    
    
    
