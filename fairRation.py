def fairRations(B):
    # Write your code here
    count=0
    for i in B:
        if i%2!=0:
            count+=1
            
    if count%2==0:
        count=0
        for i in range(len(B)):
            if B[i]%2!=0:
                B[i]+=1
                B[i+1]+=1
                count+=2
        return count
    else:
        return "NO"

    


print(fairRations([2,3,4,5]))