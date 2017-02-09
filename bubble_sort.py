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
