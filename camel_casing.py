string = 'camelCasingHaha'
stri = ''

for letter in string:
    if letter.isupper():
        stri += ' ' + letter
    else:
        stri += letter
        
print(stri)
