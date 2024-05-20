import sys
from collections import defaultdict

def hash_fun(string):
    
    res = 0
    for ch in string:
        res = ((res+ord(ch))*17)%256
    return res
    
    return curr
        
if __name__ == "__main__":
    
    inputs = sys.stdin.read().split(',')
    
    res = 0
    for i in inputs:
        res += hash_fun(i)
    print(res)
