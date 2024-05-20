import sys
from collections import deque
    
if __name__ == "__main__":
    
    inputs = sys.stdin.read().strip()
    
    inputs = inputs.split('\n\n')
    
    res = 0
    
    for temp in inputs:
        
        grid = [[i for i in row] for row in temp.split('\n')]
        
        n = len(grid)
        m = len(grid[0])
        
        for i in range(m-1):
            t1 = 0
            for j in range(m):
                l = i-j
                r = i+j+1
                
                if 0<=l<r<m:
                    for tt in range(n):
                        if grid[tt][l] != grid[tt][r]:
                            t1 += 1
            
            if t1 == 0:
                res += i+1

        for i in range(n-1):
            t1 = 0
            for j in range(n):
                u = i-j
                d = i+j+1
                
                if 0<=u<d<n:
                    for tt in range(m):
                        if grid[u][tt] != grid[d][tt]:
                            t1 += 1
            
            if t1 == 0:
                res += 100*(i+1)
                
    print(res)
                
        

