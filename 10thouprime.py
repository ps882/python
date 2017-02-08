def tenthoustprime(limit):
    count = 1
    prime = [2]
    i = 3
    while count < limit:
        for j in prime:
            if i % j == 0:
                break
        else:
            prime.append(i)
            count += 1
        i += 1
    print prime

#tenthoustprime(6)

#def trianglenum(divisors):
 #   count = 0
  #  while count <= divisors:
