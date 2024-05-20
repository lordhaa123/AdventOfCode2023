import sys
from collections import defaultdict
    
def getAnswer(grid,n,m):
    res = 0
    for i in range(n-1,-1,-1):
        curr = 0
        for j in range(m):
            if grid[i][j] == 'O':
                curr += 1
        res += (n-i)*curr
    return res

def rotateGrid(grid,n,m):
    temp = [['.' for _ in range(n)] for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            temp[j][n-1-i] = grid[i][j]
    return temp
    
def rollGrid(grid,n,m):
    for i in range(n):
        for j in range(m):
            
            curr = grid[i][j]
            if curr == '.':
                for row in range(i+1,n):
                    
                    if grid[row][j] == 'O':
                        grid[row][j] = '.'
                        grid[i][j] = 'O'
                        break
                    elif grid[row][j] == '#':
                        break
    

if __name__ == "__main__":
    
    inputs = sys.stdin.read().splitlines()
    
    inputs = [[i for i in row] for row in inputs]
    
    # for i in inputs:
    #     print(i)
        
    n = len(inputs)
    m = len(inputs[0])
    
    dp = {}
    
    num = 0
    while(num<1000000000):
        for _ in range(4):
            rollGrid(inputs,n,m)
            inputs = rotateGrid(inputs,n,m)
        
        grid = tuple(tuple(row) for row in inputs)
        
        if grid in dp:
            cl = num - dp[grid]
            if cl!=0:
                temp = (1000000000 - num)//cl
                num += temp*cl
        
        dp[grid] = num
        num+=1
    
    # for i in inputs:
    #     print(i)
    
    print(getAnswer(inputs,n,m))
        


