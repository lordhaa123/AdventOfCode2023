import sys

inputs = sys.stdin.read().splitlines()

#print(inputs)

time = inputs[0].split(" ")
time = [t for t in time if t != '']
time = time[1:]
#print(time)

dist = inputs[1].split(" ")
dist = [t for t in dist if t != '']
dist = dist[1:]
#print(dist)

res = 1

for i in range(len(time)):
    
    t = int(time[i])
    d = int(dist[i])
    temp = 0
    
    for j in range(t):
        if j*(t-j) > d:
            temp+=1
    #print(temp)
    res*=temp

print(res)
