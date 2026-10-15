'''l=input().split()
floor=0
for i in l:
    floor+=int(i)
print(floor)'''

'''
l=list(map(int,input().split()))
score=0
for i in l:
    if(i==1):
        score+=10
    else:
        score-=2
print(score)

'''

id1,id2=input().split()
flag=True
l={}
for i in range(len(id1)):
    if not id1[i] in l:
        l[id1[i]]=id2[i]
    elif l[id1[i]]!=id2[i]:
        flag=False
        break
    else:
        continue
print(flag)