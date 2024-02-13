a = 'xyaabbbccccdefww'
b = 'xxxxyyyyabklmopq'
c = a+b

letters = []

for letter in c:
    if letter not in letters:
        letters.append(letter)

longest = ''
letters.sort()
for letter in letters:
    longest += letter
    
print(longest)