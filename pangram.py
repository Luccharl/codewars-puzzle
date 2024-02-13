def is_pangram(s):
    s.lower()
    
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in s:
            return False
    return True
            
    
    
print(is_pangram('The quick brown fox jumps over the lazy dog'))