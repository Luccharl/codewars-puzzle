string = 'recede'
string = string.lower()
encoded = ''
for char in string:
    if string.count(char) == 1:
        encoded += '('
    else:
        encoded += ')'
        
print(encoded)