def multiple_regex(n):
    try:
        if int(n,2) % 3 == 0:
            return True
        else:
            return False
    except:
        return False
    
print(multiple_regex('000'))