import sys
from collections import defaultdict,deque
import heapq

if __name__ == "__main__":
    
    grid = sys.stdin.read().splitlines()
    #print(grid)
    grid = [[c for c in row] for row in grid]
    
    n = len(grid)
    m = len(grid[0])
    
    start = [(0,0,0,-1,-1)]
    q = start
    dp = {}
    while(len(q)>0):
        dist,i,j,d,max_move = heapq.heappop(q)
        
        if (i,j,d,max_move) in dp:
            continue
        
        dp[(i,j,d,max_move)] = dist
        
        for num , (dx,dy) in enumerate([[-1,0],[0,1],[1,0],[0,-1]]):
            x = i + dx
            y = j + dy
            new_d = num
            new_max_move = 1 if new_d!=d else max_move+1
            
            notReverse = ((new_d+2)%4 != d) 
            
            if 0<=x<n and 0<=y<m and new_max_move<=3 and notReverse:
                cost = int(grid[x][y])
                if (x,y,num,new_max_move) in dp:
                    continue
                heapq.heappush(q,(dist+cost,x,y,new_d,new_max_move))
    
    ans = 999999999999
    
    for (i,j,_,_),dist in dp.items():
        if i == n-1 and j == m-1:
            ans = min(ans,dist)
    
    print(ans)
        
        
    
    

