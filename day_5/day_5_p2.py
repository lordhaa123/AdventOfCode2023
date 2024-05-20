import sys

if __name__ == "__main__":
    
    with open("input.txt",'r') as f:
    	inputs = f.read().splitlines()
    #print(inputs)
    seeds = inputs[0].split(": ")[1].split(" ")
    seeds = [int(i) for i in seeds if i!=""]
    #print(seeds)
    
    mps = []
    mp = []
    for ln in inputs[1:]:
        if ln == "":
            if mp:
                mps.append(mp)
                mp = []
        else:
            mp.append(ln)
    
    if mp:
        mps.append(mp)
    #print("maps are done")       
    def getValue(src):
        temp = src
        for mp in mps:
            m = mp[1:]
            for i in m:
                i = [int(x) for x in i.split(" ")]
                src_range = range(i[1],i[1]+i[2])
                
                if temp in src_range:
                    dist = temp - i[1]
                    temp = i[0] + dist
                    #print(temp,end="->")
                    break
        return temp
        
    mini = 999999999999
    
    #print("starting seeds")
    vis = set()
    print(len(seeds))
    for i in range(0,len(seeds),2):
        print(i)
        for seed in range(seeds[i],seeds[i]+seeds[i+1]):
            if seed not in vis:
                mini = min(mini,getValue(i))
                vis.add(seed)

    
    print(min(lis))
    
    


