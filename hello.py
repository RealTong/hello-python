def findMinAndMax(L):
    if L != []:
        max = L[0]
        min = L[0]
        for i in L:
            if(max <= i):
                max = i
            if(min >= i):
                min = i
    return max,min


print(findMinAndMax([10,50,60,2,7,100,25]))

print([x*x for x in range(1,11)if x%2==0])