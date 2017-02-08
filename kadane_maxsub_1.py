def max_sub(A):
    maxend = maxfin = A[0]
    startindex = endindex = 0
    idx = 1
    for i in A[1:]:
        #print i , maxend
        if maxend + i < i:
            #print i , maxend
            startindex = idx
        maxend = max(i , maxend + i)
        if maxfin < maxend:
            endindex = idx
        maxfin = max(maxfin , maxend)
        idx += 1
    if startindex > endindex:
        startindex = endindex
    return maxfin , startindex , endindex


A = [2 , 4, -5 , 2 , -5 , 5 , -1 , 4]
B = [2 , -4, -5 , -2 , -5 , -5 , -1 , -4]
print max_sub(A)