import sys
from collections import defaultdict
 
def hash_fun(string):
    
    res = 0
    for ch in string:
        res = ((res+ord(ch))*17)%256
    return res

if __name__ == "__main__":
    
    inputs = sys.stdin.read().split(',')
    #print(inputs)
    
    boxes = [[] for _ in range(256)]
    
    for string in inputs:
        #print(hash_fun(string))
        if string[-1]=='-':
            name = string[:-1]
            h = hash_fun(name)
            boxes[h] = [(n,x) for (n,x) in boxes[h] if n!=name]
        elif string[-2]=='=':
            name = string[:-2]
            h = hash_fun(name)
            num = int(string[-1])
            if name in [n for (n,x) in boxes[h]]:
                boxes[h] = [(n, num if name==n else x) for (n,x) in boxes[h]]
            else:
                boxes[h].append((name, num))
    
    # for box in boxes:
    #     print(box)
    
    res = 0
    
    for i,box in enumerate(boxes):
        for j,(n,x) in enumerate(box):
            res += (i+1)*(j+1)*x
    
    print(res)
