import sys

inputs = sys.stdin.read().splitlines()

#print(inputs)

time = inputs[0].split(" ")
time = [t for t in time if t != '']
time = time[1:]
tt = ""
for i in time:
    tt+=i
print(tt)

dist = inputs[1].split(" ")
dist = [t for t in dist if t != '']
dist = dist[1:]
dd = ""
for i in dist:
    dd += i
print(dd)

res = 0
tt = int(tt)
dd = int(dd)

for i in range(tt):
    if i*(tt-i) > dd:
        res+=1
        
print(res)
