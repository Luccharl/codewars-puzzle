from math import sqrt


square = 114

root = sqrt(square)
if root%1 == 0:
    next_square = int((root+1)**2)
    print(next_square)
else:
    print(-1)
    