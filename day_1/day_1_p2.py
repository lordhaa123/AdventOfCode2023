from sys import stdin

mp = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
}

def wordToDigit(s:str, lis):
    

    for word,num in sorted(mp.items()):
        temp = s
        #print(num)
        #s = s.replace(word,num)
        
        while(temp.find(word)!=-1):
            lis.append((num,temp.find(word)))
            temp=temp.replace(word,"*"*len(word),1)
        
    return s
    
if __name__ == "__main__":
    
    res = 0
    
    for line in open("input.txt",'r').readlines():
        #print(line)
        first = -1
        last = -1
        line = line
        lis = []
        line = wordToDigit(line,lis)
        
        #print(line,end = " ")
        
        for (i,ch) in enumerate(line):
            if ch!='/n' and ch.isdigit():
                lis.append((ch,i))
                
        lis = sorted(lis,key = lambda x:x[1])
        first = lis[0][0]
        last = lis[-1][0]
        #print(first+last)
        if(first != -1 and last != -1):
            res += int(first+last)
    
    print(res)
            

