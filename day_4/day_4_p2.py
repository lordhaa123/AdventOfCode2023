import sys
from collections import defaultdict

if __name__ == "__main__":

    inputs = defaultdict(list) 
    idx = 0
    for line in sys.stdin:
        ln = line.split(':')[1][:-1]
        inputs[idx].append(ln.split('|'))
        idx += 1
    
    res = 0
    for game in inputs.keys():
        res += len(inputs[game])
        for gg in inputs[game]:
            #print(gg)
            mp = defaultdict()
            keys = gg[0].split(" ")
            keys = [i for i in keys if i != '']
            #print(keys)
            values = gg[1].split(" ")
            values = [i for i in values if i != '']
            #print(values)
            n = 0
            for val in values:
                if val in keys:
                    n+=1
            break
        for _ in range(len(inputs[game])):
            for i in range(1,n+1):
                curr = i+game
                curr_list = inputs[curr][0]
                inputs[curr].append(curr_list)
        
    print(res)





