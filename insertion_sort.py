def insertion_sort(list):
    for idx in range(1,len(list)):
        elem = list[idx]
        for jdx in range(idx,-1,-1):
            if elem < list[jdx]:
                list[jdx],list[jdx+1] = list[jdx+1] , list[jdx]
    return list

mylist = [1233,2,5,23,13,98,654,2,6,3,2]
#print insertion_sort(mylist)