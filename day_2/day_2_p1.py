import sys

if __name__ == "__main__":
    
    idx = 0
    res = 0
    for line in sys.stdin:
        
        idx += 1
        
        line = line.split(':')
        line = line[-1]
        
        groups = line.split(';')
        

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
                
            if blue > 14 or red > 12 or green > 13:
                flag = False
                        
        if flag == True:
            #print(groups , end = ' ')
            #print(idx)
            res += idx
    print(res)
