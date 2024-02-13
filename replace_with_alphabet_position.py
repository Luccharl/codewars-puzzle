from turtle import pos


string = 'The'
alphabets='abcdefghijklmnopqrstuvwxyz'

position = []
replace = ''

for letter in string:
    if letter.lower() in alphabets:
        position.append(str(alphabets.index(letter.lower())+1))
        
strs = ' '.join(position)
    
print(strs)