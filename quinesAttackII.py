def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    temp=[[0 for j in range(n)] for i in range(n)]
    temp[(r_q-1)][(c_q-1)]=8
    if k>0:
        for i in obstacles:
            temp[i[0]-1][i[1]-1]=2

    for i in range(c_q,n):
        if temp[r_q-1][i]==0:
            temp[r_q-1][i]=1
        else:
            break
    for i in range(c_q-2,-1,-1):
        if temp[r_q-1][i]==0:
            temp[r_q-1][i]=1
        else:
            break
    for i in range(r_q,n):
        if temp[i][c_q-1]==0:
            temp[i][c_q-1]=1
        else:
            break
    for i in range(r_q-2,-1,-1):
        if temp[i][c_q-1]==0:
            temp[i][c_q-1]=1
        else:
            break

    i=r_q
    j=c_q
    while i<n and j<n:
        if temp[i][j]==0:
            temp[i][j]=1
        else:
            break
        i+=1
        j+=1
    i=r_q-2
    j=c_q-2
    while i>-1 and j>-1:
        if temp[i][j]==0:
            temp[i][j]=1
        else:
            break
        i-=1
        j-=1
    i=r_q
    j=c_q-2
    while i<n and j>-1:
        if temp[i][j]==0:
            temp[i][j]=1
        else:
            break
        i+=1
        j-=1
    i=r_q-2
    j=c_q
    while i>-1 and j<n:
        if temp[i][j]==0:
            temp[i][j]=1
        else:
            break

        i-=1
        j+=1

    count=0
    for i in temp:
        for j in i:
            if j==1:
                count+=1
 
    return count


print(queensAttack(100000,0,4187,5068,[]))