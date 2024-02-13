import random
from re import T

direction = ['n','s','e','w']
walk = ['n','s','n','s','n','s','n','s','n','s']
#walk = ['a','b','c','d','e','f','g','h','i','j']

# random.shuffle(direction)
# num = random.randint(1,10)

# for i in range(num):
#     chosen_dir = random.choice(direction)
#     walk.append(chosen_dir)

if len(walk) == 10:
    if walk[1:5] == walk[:-5:-1]:
        print(True)
    else:
        print(False)
else:
    print(False)