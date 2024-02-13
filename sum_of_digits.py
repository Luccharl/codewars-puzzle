def digital_root(n):
    sum = 0

    n = str(n)
    while True:
        for digit in n:
            sum += int(digit)
        n = str(sum)
        sum = 0

        if len(n) > 1:
            continue
        else:
            break
    return int(n)

print(digital_root('12345'))
    
    
    
        