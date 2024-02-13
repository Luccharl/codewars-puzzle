def is_isogram(string):
    word = {}
    dupes = 0
    
    for letter in string.lower():
        if letter in word:
            word[letter] += 1
        else:
            word[letter] = 1
    
    for letter in word.values():
        if letter > 1:
            dupes += 1
        else:
            continue
    
    if dupes >= 1:
        return False
    else:
        return True
    
print(is_isogram('Dermatoglyphics'))