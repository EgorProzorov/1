with open('17-1.txt') as f:
    a=[int(x) for x in f.readlines()]
count=0
ma=0
for i in range(len(a)-1):
    if a[i]<a[i+1] and a[i]>a[i-1]:
        count+=1
        ma=max(ma,a[i])
print(count,ma)
