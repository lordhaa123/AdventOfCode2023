import sys
from collections import defaultdict

if __name__ == "__main__":

    inputs = []    
    
    for line in sys.stdin:
        ln = line.split(':')[1][:-1]
        inputs.append(ln.split('|'))
        
    res = 0
    for game in inputs:
        mp = defaultdict()
        keys = game[0].split(" ")
        keys = [i for i in keys if i != '']
        #print(keys)\
        values = game[1].split(" ")
        values = [i for i in values if i != '']
        #print(values)
        n = -1
        for val in values:
            if val in keys:
                n+=1
        
        if n>=0:
            res += 2**n
        
    print(inputs)





