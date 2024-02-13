def xo(string):
    string = string.lower()
    x_count = 0
    o_count = 0
    
    for xo in string:
        if 'x' in xo:
            x_count += 1
        if 'o' in xo:
            o_count += 1
        
    if x_count == o_count:
        return True
    else:
        return False
        
#efficient
def xo(string):
    string = string.lower()
    return string.count('x') == string.count('o')
