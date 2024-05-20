import sys

def getNext(lis):
    
    n = len(lis)
    if n <= 2:
        return lis[-1] + (lis[1]-lis[0])
    
    if [0]*n == lis:
        return 0
        
    temp = []
    for i in range(n-1):
        temp.append(lis[i+1]-lis[i])
    
    diff = getNext(temp)
    return lis[-1]+diff
    
if __name__ == "__main__":
    inputs = sys.stdin.read().splitlines()
    
    #print(inputs)
    
    rows = [i.split(" ") for i in inputs]
    
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            rows[i][j] = int(rows[i][j])
    
    #print(rows)
    
    res = 0
    for row in rows:
        res += getNext(row)
    
    print(res)
    
    
