def power_sumDigTerm(n):
    num_pow = []
    index = n - 1
    sum = 0
    for a in range(2, 99):
        for b in range(2, 20):
            c = a**b
            for dig in str(c):
                sum += int(dig)
            if a == sum:
                num_pow.append(c)
            sum=0

    num_pow.sort()

    return num_pow[index]