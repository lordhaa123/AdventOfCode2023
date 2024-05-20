import sys
from collections import defaultdict

dp = defaultdict()

def helper(row, groups, i, j, curr):
    key = (i, j, curr)
    if key in dp:
        return dp[key]
    if i==len(row):
        if j==len(groups) and curr==0:
            return 1
        elif j==len(groups)-1 and blocks[j]==curr:
            return 1
        else:
            return 0
      
    ans = 0
    for c in ['.', '#']:
    
        if row[i]==c or row[i]=='?':
            if c=='.' and curr==0:
                ans += helper(row, groups, i+1, j, 0)
            
            elif c=='.' and current>0 and j<len(blocks) and groups[j]==curr:
                ans += helper(row, groups, i+1, j+1, 0)
            
            elif c=='#':
                ans += helper(row, groups, i+1, j, curr+1)
        
        dp[key] = ans
        
        return ans

if __name__ == '__main__':

    inputs = sys.stdin.read().strip()
    temp = inputs.split('\n')
    
    
    res = 0
    for line in temp:
        row,groups = line.split()
        row = '?'.join([row, row, row, row, row])
        groups = ','.join([groups, groups, groups, groups, groups])
        groups = [int(x) for x in groups.split(',')]
        dp.clear()
        score = helper(row, groups, 0, 0, 0)
        res += score
    print(res)
        
        
        
    
