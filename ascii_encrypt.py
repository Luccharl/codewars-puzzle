string = 'A hello'
words = string.split()

code = []

for word in words:
    encoded = ''
    first_letter = word[:1]
    last_letter = word[-1]
    sec_letter = word[1:2]
    remaining_letter = word[2:-1]
    ascii_val = ord(first_letter)

    if len(word) == 2:
        encoded = f'{ascii_val}{last_letter}{remaining_letter}'
    elif len(word) > 2:
        encoded = f'{ascii_val}{last_letter}{remaining_letter}{sec_letter}'
    else:
        encoded = f'{ascii_val}{remaining_letter}{sec_letter}'
    
    code.append(encoded)
    
print(' '.join(code))
