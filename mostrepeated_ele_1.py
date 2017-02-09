def findrepeated(a):
    dict = {}
    for idx in range(len(a)):
        if a[idx] in dict:
            dict[a[idx]] += 1
        else:
            dict[a[idx]] = 1
    max = -9999999
    max_elem = 0
    for elem in dict:
        if dict[elem] > max:
            max = dict[elem]
            max_elem = elem
    return max_elem

mylist = [4, 5 ,6,4,4,4,4 ,234,23,5 ,5,3,4, 34,3]
#print findrepeated(mylist)

def find_max_sequence(a):
    max_len = 1
    max_endidx = 0
    temp_len = 1
    for idx in range(len(a)-1):
        if a[idx]+1 == a[idx+1]:
            temp_len += 1
        else:
            if max_len < temp_len:
                max_len = temp_len
                max_endidx = idx
            temp_len = 1
    else:
        if max_len < temp_len:
            max_len = temp_len
            max_endidx = idx+1

    return max_endidx-max_len+1,max_endidx

mylist = [1,2,345,346,347,2,6,7,8,9,10,11,12,13]
#print find_max_sequence(mylist)

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

def insertion_sort(list):
    for idx in range(1,len(list)):
        elem = list[idx]
        for jdx in range(idx,-1,-1):
            if elem < list[jdx]:
                list[jdx],list[jdx+1] = list[jdx+1] , list[jdx]
    return list

mylist = [1233,2,5,23,13,98,654,2,6,3,2]
#print insertion_sort(mylist)

import timeit

def bubble_sort(list):
    for _ in range(len(list)):
        for idx in range(len(list)-1):
            if list[idx] > list[idx+1]:
                list[idx] , list[idx+1] = list[idx+1] , list[idx]
    return list

mylist = [1233,2,5,23,13,98,654,2,6,3,2]
start = timeit.timeit()
print bubble_sort(mylist)
print timeit.timeit() - start

def bubble_sort_improved(list):
    for iteration in range(len(list)):
        for idx in range(len(list) -1 - iteration):
            if list[idx] > list[idx+1]:
                list[idx] , list[idx+1] = list[idx+1] , list[idx]
    return list

mylist = [1233,2,5,23,13,98,654,2,6,3,2]
start = timeit.timeit()
print bubble_sort_improved(mylist)
print timeit.timeit() - start

def bubble_sort_improved2(list):
    for iteration in range(len(list)):
        sorted = 0
        for idx in range(len(list) - 1 - iteration):
            if list[idx] > list[idx+1]:
                list[idx] , list[idx+1] = list[idx+1] , list[idx]
                sorted = 1
        if sorted == 0:
            break
    return list

mylist = [1233,2,5,23,13,98,654,2,6,3,2]
start = timeit.timeit()
print bubble_sort_improved2(mylist)
print timeit.timeit() - start
#output
#[2, 2, 2, 3, 5, 6, 13, 23, 98, 654, 1233]
#-0.00337162470136
#[2, 2, 2, 3, 5, 6, 13, 23, 98, 654, 1233]
#-0.00135060931375
#[2, 2, 2, 3, 5, 6, 13, 23, 98, 654, 1233]
#-0.000743185021346
