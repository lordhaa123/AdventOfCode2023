import sys
from collections import deque
    
if __name__ == "__main__":
    
    graph = sys.stdin.read().splitlines()
    
    # for i in graph:
    #     print(i)

    n = len(graph)
    m = len(graph)
    
    start = (0,0)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'S':
                start = (i,j)
    
    possible_starts = []
    i,j = start
    if i>0:
        if graph[i-1][j] in ['7','F','|']:
            possible_starts.append((i-1,j))
    if i<n-1:
        if graph[i+1][j] in ['L','J','|']:
            possible_starts.append((i+1,j))
    if j>0:
        if graph[i][j-1] in ['F','L','-']:
            possible_starts.append((i,j-1)) 
    if j<n-1:
        if graph[i][j+1] in ['J','7','-']:
            possible_starts.append((i,j+1))  
                
    print(possible_starts)
    
    vis = set()
    
    que = deque(possible_starts)
    
    for curr in possible_starts:
        vis.add(curr)
    
    count = 0
    
    while(len(que)>0):
        count+=1
        l = len(que)
        while(l>0):
            l-=1
            x,y = que.pop()
            if (x,y) == start:
                break
            if graph[x][y] == '|':
                if x-1 >= 0:
                    if (x-1,y) not in vis:
                        if graph[x-1][y] in ['|','F','7']:
                            vis.add((x-1,y))
                            que.appendleft((x-1,y))
                if x+1<n:
                    if (x+1,y) not in vis:
                        if graph[x+1][y] in ['|','J','L']:
                            vis.add((x+1,y))
                            que.appendleft((x+1,y))
            elif graph[x][y] == '-':
                if y-1 >= 0:
                    if (x,y-1) not in vis:
                        if graph[x][y-1] in ['-','F','L']:
                            vis.add((x,y-1))
                            que.appendleft((x,y-1))
                if y+1 < m:
                    if (x,y+1) not in vis:
                        if graph[x][y+1] in ['-','J','7']:
                            vis.add((x,y+1))
                            que.appendleft((x,y+1))
            elif graph[x][y] == 'L':
                if x-1 >= 0:
                    if (x-1,y) not in vis:
                        if graph[x-1][y] in ['|','F','7']:
                            vis.add((x-1,y))
                            que.appendleft((x-1,y))
                if y+1<m:
                    if (x,y+1) not in vis:
                        if graph[x][y+1] in ['-','J','7']:
                            vis.add((x,y+1))
                            que.appendleft((x,y+1))
            elif graph[x][y] == 'J':
                if x-1 >= 0:
                    if (x-1,y) not in vis:
                        if graph[x-1][y] in ['|','F','7']:
                            vis.add((x-1,y))
                            que.appendleft((x-1,y))
                if y-1 >= 0:
                    if (x,y-1) not in vis:
                        if graph[x][y-1] in ['-','F','L']:
                            vis.add((x,y-1))
                            que.appendleft((x,y-1))
            elif graph[x][y] == '7':
                if x+1<n:
                    if (x+1,y) not in vis:
                        if graph[x+1][y] in ['|','J','L']:
                            vis.add((x+1,y))
                            que.appendleft((x+1,y))                
                if y-1 >= 0:
                    if (x,y-1) not in vis:
                        if graph[x][y-1] in ['-','F','L']:
                            vis.add((x,y-1))
                            que.appendleft((x,y-1))
            elif graph[x][y] == 'F':
                if x+1<n:
                    if (x+1,y) not in vis:
                        if graph[x+1][y] in ['|','J','L']:
                            vis.add((x+1,y))
                            que.appendleft((x+1,y))                                
                if y+1<m:
                    if (x,y+1) not in vis:
                        if graph[x][y+1] in ['-','J','7']:
                            vis.add((x,y+1))
                            que.appendleft((x,y+1))     
    
    print(count)
                
            
            
    
