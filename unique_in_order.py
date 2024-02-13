seq = 'AAAABBBCCDAABBB'
char = ''
order = []

for i in seq:
    if char != i:
        order.append(i)
        char = i 

print(order)
    