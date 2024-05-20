import sys
from collections import defaultdict,deque

if __name__ == "__main__":
    
    grid = sys.stdin.read().splitlines()
    #print(grid)
    grid = [[c for c in row] for row in grid]
    
    # for i in grid:
    #     print(i)

    direction = [0,0,1,0]
    
    n = len(grid)
    m = len(grid[0])
    
    start = (0,-1,0,1)
    vis = set()
    q = deque([start])
    #vis.add(start)
    while(len(q)>0):
        
        i,j,di,dj = q.pop()
        i+=di
        j+=dj
        #print(i,j,di,dj)
        if i < 0 or i >= n or j < 0 or j >= m:
            continue
        
        curr = grid[i][j]
        
        if curr == "." or (curr == "-" and dj != 0) or (curr == "|" and di != 0):
            if (i, j, di, dj) not in vis:
                vis.add((i, j, di, dj))
                q.append((i, j, di, dj))
                
        elif curr == "/":
            di, dj = -dj, -di
            if (i, j, di, dj) not in vis:
                vis.add((i, j, di, dj))
                q.append((i, j, di, dj))
                
        elif curr == "\\":
            di, dj = dj, di
            if (i, j, di, dj) not in vis:
                vis.add((i, j, di, dj))
                q.append((i, j, di, dj))
                
        else:
            if curr == '|':
                for di,dj in [(1, 0), (-1, 0)]:
                    if (i, j, di, dj) not in vis:
                        vis.add((i, j, di, dj))
                        q.append((i, j, di, dj))
            else:
                for di, dj in [(0, 1), (0, -1)]:
                    if (i, j, di, dj) not in vis:
                        vis.add((i, j, di, dj))
                        q.append((i, j, di, dj))
    
    res = len({(i,j) for (i,j,_,_) in vis})
    print(res)   
    
