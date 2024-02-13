string = 'hi there'
vowels = 'aeiou'
num = '12345'
code = ''
decoded = ''

for char in string:
    if char in vowels:
        code += str(vowels.index(char)+1)
    else:
        code += char
        
print(code)

for char in code:
    if char in num:
        decoded += vowels[num.index(char)]
    else:
        decoded += char

print(decoded)
