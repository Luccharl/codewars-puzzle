string = 'This website is for losers LOL!.'

def disemvowel(string_):
    vowels = 'aeiou'
    
    for letter in string_:
        if letter.lower() in vowels:
            copy = string_.replace(letter, '')
            string_ = copy
        
    return string_

print(disemvowel(string))
