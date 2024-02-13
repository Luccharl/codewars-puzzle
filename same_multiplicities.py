a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]


from math import sqrt

def comp(a, b):
    new_list = []
    
    if a == [] or b == [] :
        return False
    else:
        for num in b:
            if sqrt(num) in a:
                new_list.append(num)
            
        if len(new_list) == len(a):
            return True
        else:
            return False
        
print(comp(a,b))