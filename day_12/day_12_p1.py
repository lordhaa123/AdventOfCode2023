import sys
    
def findGroups(row):
    res = []
    
    count = 0
    for i in range(len(row)):
        if row[i] == '#':
            count += 1
        else:
            if count>0:
                res.append(str(count))
                count = 0
    
    if count>0:
        res.append(str(count))
    return res

def findArrangements(row,groups):
    
    indices = []
    for i in range(len(row)):
        if row[i] == '?':
            indices.append(i)
    
    n = len(indices)
    #print(bin(n).replace("0b", ""))
    
    count = 0
    
    for i in range(2**n):
        temp = row.copy()
        bin_i = bin(i).replace("0b", "")
        bin_i = (n-len(bin_i))*'0' + bin_i
        #print(bin_i)
        for j in range(n):
            if bin_i[j] == '0':
                temp[indices[j]] = '.'
            else:
                temp[indices[j]] = '#'
        
        curr_grp = findGroups(temp)
        #print(curr_grp , groups)
        
        if curr_grp == groups:
            count+=1
    
    return count
    
    

    
if __name__ == "__main__":
    
    inputs= open("input.txt",'r').read().strip()
    temp = inputs.split('\n')
    grid = [[c for c in row] for row in temp]
    
    #print(grid)
    rows = []
    
    for i in grid:
        idx = i.index(' ')
        new_temp = i[idx+1:]
        lis = []
        curr = ""
        for j in new_temp:
            if j == ',':
                lis.append(curr)
                curr = ""
            else:
                curr += j
        if curr != "":
            lis.append(curr)
        rows.append([i[:idx],lis])
    
    res = 0
    for i in rows:
        res += findArrangements(i[0],i[1])
    print(res)
    
    
    
    