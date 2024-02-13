string = 'seTrreess'
low = string.lower()

non_repeat = []

for char in string:
    repeat = low.count(char.lower())       
    if char not in non_repeat and repeat == 1:
        non_repeat.append(char)
   
if not non_repeat:
    print(True)
else:
    print(non_repeat[0])
    
enumerate
