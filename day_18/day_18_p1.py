import sys
from collections import defaultdict,deque
import heapq

if __name__ == "__main__":
    
    grid = sys.stdin.read().splitlines()
    
    grid = [i.split() for i in grid]
    
    perimeter = 0
    inner_area = 0
    y = 0
    for i in grid:
        perimeter += int(i[1])
        
        if i[0] == 'R':
            inner_area += y*int(i[1])
        elif i[0] == 'L':
            inner_area -= y*int(i[1])
        elif i[0] == 'U':
            y += int(i[1])
        elif i[0] == 'D':
            y -= int(i[1])
    
    ans = inner_area + perimeter//2 + 1

    print(ans)
