def most_frequent(l):
    dict={}
    for i in l:
        dict[i]=l.count(i)
    mf=-1
    num=0
    for i in dict:
        if dict[i]>mf:
            mf=dict[i]
            num=i
        else:
            if dict[i]==mf and num>i:
                num=i
    return num

l=[1,2,2,2,2,3,3,3,3,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
print(most_frequent(l))