def merge_sort(A):
    if len(A) != 1:
        x1 = merge_sort(A[:len(A)/2])
        x2 = merge_sort(A[len(A)/2:])
        #print "merged values are " , merge(x1,x2)
        return merge(x1,x2)
    else:
        #print "single values are " , A
        return A

def merge(x1,x2):
    n = len(x1) + len(x2)
    merged = []
    i = j = 0
    for _ in range(n):
        if x1[i] < x2[j]:
            merged.append(x1[i])
            i += 1
            if i >= len(x1):
                break
        else:
            merged.append(x2[j])
            j += 1
            if j >= len(x2):
                break
    if i < len(x1):
        for idx in range(i,len(x1)):
            merged.append(x1[idx])
    if j < len(x2):
        for idx in range(j,len(x2)):
            merged.append(x2[idx])
    return merged

a = [5,3,4,1,10,2,9,34,231,23,5,2343434,534]
#print merge_sort(a)