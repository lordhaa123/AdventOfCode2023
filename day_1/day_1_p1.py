from sys import stdin

if __name__ == "__main__":
    
    res = 0
    
    for line in open("input.txt",'r').readlines():
        print(line)
        first = -1
        last = -1
        
        for (i,ch) in enumerate(line):
            if ch != '\n' and ch.isdigit():
                if first == -1:
                    first = i
                    last = i
                else:
                    last = i
        # print(line[first],end = "")
        # print(line[last] , end = '\n')
        if(first != -1 and last != -1):
            res += int(line[first] + line[last])
    
    print(res)
            
