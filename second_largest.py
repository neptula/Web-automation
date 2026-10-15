l=[int(x) for x in input().split()]
a=-1
b=-1
for i in range(len(l)):
    if a<l[i]:
        b=a
        a=l[i]
    elif l[i]>b:
        b=l[i]
        
print(b)
