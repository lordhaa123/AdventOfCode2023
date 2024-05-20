import sys

if __name__ == "__main__":
    
    graph = []
    for line in sys.stdin:
        if line[-1] == '\n':
            graph.append([*line[:-1]])
        else:
            graph.append([*line])
       
        
    for ln in graph:
        i = 0
        while(i<len(ln)):
            if ln[i].isnumeric():
                res = ln[i]
                j = i+1
                #print(i)
                while(j<len(ln)):
                    if ln[j].isnumeric():
                        res+=ln[j]
                    else:
                        for idx in range(i,j):
                            #print(res)
                            ln[idx] = res
                        i = j+1
                        j = len(ln)
                    j+=1
                else:
                    if j == len(ln):
                        for idx in range(i,j):
                            #print(res)
                            ln[idx] = res
                        i = j+1
                        j = len(ln)
            else:
                if i < len(ln):
                    i+=1
    
    res = 0
    n = len(graph)
    m = len(graph[0])
    dir = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

    # for i in graph:
    #     print(i)

    #vis = set()
    for i in range(n):
        for j in range(m):
            if not graph[i][j].isalnum() and graph[i][j] != '.':
                for dx,dy in dir:
                    x = i+dx
                    y = j+dy
                    if x<n and x>=0 and y<m and y>=0:
                        if graph[x][y].isdigit(): 
                            curr = int(graph[x][y])
                            #print(curr,x,y)
                            res += curr
                            temp = graph[x][y]
                            new_y = y
                            flag = True
                            while(new_y>=0 and flag == True):
                                #print(x,new_y , graph[x][new_y])
                                if graph[x][new_y] == temp:
                                    graph[x][new_y] = '.'
                                else:
                                    flag = False
                                new_y -= 1
                                
                            new_y = y+1
                            flag = True
                            while(new_y<m and flag == True):
                                #print(x,new_y)
                                if graph[x][new_y] == temp:
                                    graph[x][new_y] = '.'
                                else:
                                    flag = False
                                new_y += 1
                            
    
    # print()
    # for i in graph:
    #     print(i)
    print(res)




