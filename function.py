def most_frequent(l):
    dict={}
    for i in l:
        dict[i]=l.count(i)
    res=[]
    for i in dict:
        if dict[i]==2:
            res.append(i)
    res.sort()
    if len(res)==0:
        return -1
    else:
        return res

l=input().split()
l=[int(x) for x in l]
len= most_frequent(l)
for i in len:
    print(i,end=" ")