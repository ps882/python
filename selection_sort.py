def selection_sort(list):
    for idx in range(len(list)):
        min = idx
        for jdx in range(idx, len(list)):
            if list[min] > list[jdx]:
                min = jdx
        list[min] , list[idx] = list[idx] , list[min]
    return list

mylist = [2,5,2,654,2,6,3,2]
#print selection_sort(mylist)
