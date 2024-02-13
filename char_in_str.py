string = ''

count = {}

for char in string:
    if char not in count:
        count.setdefault(char, 1)
    else:
        count[char] += 1
    
print(count) 
        