a=[1,1,1,1,1,1,2,3,4,-1,-2,-3,-4,5,-5]
c=0
l=0
h={}
x=12
for i in range(len(a)):
    c+=a[i]
    if a[i]==x and l==0:
        l=1
    if c is x:
        l=i+1
        #print(i,end=' ')
    if c in h:
        l=max(l,i-h[c])
    else:
        h[c]=i
print(l)