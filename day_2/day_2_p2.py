import sys

if __name__ == "__main__":
    
    idx = 0
    res = 0
    for line in sys.stdin:
        
        idx += 1
        
        line = line.split(':')
        line = line[-1]
        
        groups = line.split(';')
        
        r = 0
        b = 0
        g = 0
        flag = True

        for (i,grp) in enumerate(groups):
            
            green = 0
            blue = 0
            red = 0
            items = grp.split(" ")
            for i in range(0,len(items)-1): 

                if items[i+1] == 'blue,' or items[i+1] == 'blue' or items[i+1] == 'blue\n':
                    blue = int(items[i])
                elif items[i+1] == 'red,' or items[i+1] == 'red' or items[i+1] == 'red\n':
                    red = int(items[i])
                elif items[i+1] == 'green,' or items[i+1] == 'green' or items[i+1] == 'green\n':
                    green = int(items[i])
                
            r = max(r,red)
            b = max(b,blue)
            g = max(g,green)
            #print(r,b,g)
        temp = 1 
        if r != 0:
            temp*=r
        if b != 0:
            temp*=b
        if g != 0:
            temp*=g
        res += temp
    print(res)

