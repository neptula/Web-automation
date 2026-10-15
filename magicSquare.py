def magic_square(n):
    l=[]
    for i in range(n):
        m=[]
        for j in range (n):
            m.append(0)
        l.append(m)

    i=n//2
    j=n-1
    num=n*n
    count =1
    while count<=num:
        if i==-1 and j==n:
            j=n-2
            i=0
        else:
            if j==n:
                j=0
            if i==-1:
                i =n-1
        if l[i][j] != 0:
            j=j-2
            i=i+1
            continue
        else:
            l[i][j]=count
            count+=1

            i=i-1
            j=j+1

    for i in range(n):
        for j in range(n):
            print(l[i][j],end=" ")
        print()

magic_square(3)