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
