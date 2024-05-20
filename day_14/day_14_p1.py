import sys
from collections import deque
    
def getAnswer(grid,n,m):
    res = 0
    for i in range(n-1,-1,-1):
        curr = 0
        for j in range(m):
            if grid[i][j] == 'O':
                curr += 1
        res += (n-i)*curr
    return res

if __name__ == "__main__":
    
    inputs = sys.stdin.read().splitlines()
    
    inputs = [[i for i in row] for row in inputs]
    
    # for i in inputs:
    #     print(i)
        
    n = len(inputs)
    m = len(inputs[0])
    
    for i in range(n):
        for j in range(m):
            
            curr = inputs[i][j]
            if curr == '.':
                for row in range(i+1,n):
                    
                    if inputs[row][j] == 'O':
                        inputs[row][j] = '.'
                        inputs[i][j] = 'O'
                        break
                    elif inputs[row][j] == '#':
                        break
    
    # for i in inputs:
    #     print(i)
    
    print(getAnswer(inputs,n,m))
        

