with open('17-2.txt') as f:
    a = [int(x) for x in f.readlines()]
count=0
ma=0
pos=100000
for i in range(len(a)-1):
    ma=max(ma,a[i])
for i in range(len(a)-1):
    if a[i]==ma:
        count+=1
        pos = min(pos,i+1)
print(count,pos)
