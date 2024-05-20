import sys
from collections import defaultdict,deque
import heapq

class scraps:
    def __init__(self,x,m,a,s):
        self.mp = {
            'x' : x,
            'm' : m,
            'a' : a,
            's' : s
        }
    
    def sum(self):
        return self.mp['x'] + self.mp['m'] + self.mp['a'] + self.mp['s']
    
    def print(self):
        print(self.mp)

if __name__ == "__main__":
    
    inputs = sys.stdin.read().splitlines()
    #print(inputs)
    idx = inputs.index("")
    
    flow = inputs[:idx]
    objs = inputs[idx+1:]
    
    # print(flow)
    # print(objs)
    
    flow_map = {}
    
    for f in flow:
        idx = f.find('{')
        flow_map[f[:idx]] = f[idx+1:-1].split(',')
    
    print(flow_map)
    
    lis = []
    for i in objs:
        temp = i.split(',')
        xd = []
        for j in temp:
            idx = j.find('=')
            xd.append(j[idx+1:])
        lis.append(scraps(int(xd[0]),int(xd[1]),int(xd[2]),int(xd[3][:-1])))
    
    # for i in lis:
    #     i.print()

    ops = {
        '<' : int.__lt__,
        '>' : int.__gt__
    }    

    res = 0

    for i in lis:
        f = 'in'
        #print(start_flow)
        while(True):
            #print(f)
            currFlow = flow_map[f]
            flag = False
            for j in currFlow:
                iii = j.find(':')
                if iii != -1:
                    comp = j[0]
                    op = j[1]
                    num = int(j[2:iii])
                    dest = j[iii+1:]
                    #print(comp,op,dest,num,i.mp[comp])
                    if ops[op](i.mp[comp],num):
                        if dest == 'R':
                            #print('Rejected')
                            flag = True
                            break
                        if dest == 'A':
                            #print('accepted')
                            flag = True
                            #print(i.mp,i.sum())
                            res += i.sum()
                            break
                        f = dest
                        break
                else:
                    if j == 'R':
                        #print('Rejected')
                        flag = True
                    elif j == 'A':
                        #print('accepted')
                        #print(i.mp , i.sum())
                        flag = True
                        res += i.sum()
                    else:
                        f = j
            if flag == True:
                break
                
    print(res)
    
    
