prime = []
x = range(1,int(raw_input()))
for i in x:
    if i == 1:
        print i , " not prime"
        continue
    if i == 2:
        print i," prime"
        prime.append(i)
        continue
    for j in prime:
        if i % j == 0 and j < (int(i**.5) + 1):
            print "divisible by " , j
            print i ," not prime"
            break
    else:
        print i , " prime"
        prime.append(i)