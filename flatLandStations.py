def spaceStation(n,c):
    maxm=0
    c.sort()
    m=len(c)
    if m==1:
        return max(c[0]-0,n-1-c[0])
    else:
        gaps=[]
        for i in range(1,m):
            gaps.append(c[i]-c[i-1])

        return max(c[0]-0,m-1-c[0],max(gaps)//2)


print(spaceStation(6,[0]))