def largest_prime(a):
    i = 1
    factors = []
    while a != 1:
        i += 1
        if a % i == 0:
            a = a / i
            factors.append(i)
            while a % i == 0:
                a = a / i
    print factors

#largest_prime(23422888)