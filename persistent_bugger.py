def persistence(num):
    num = str(num)
    prod = 1
    count = 0

    while len(num) > 1:
        for n in range(len(num)):
            prod *= int(num[n]) 

        num = str(prod) 
        prod = 1
        count += 1 
    
    return count

print(persistence(4))