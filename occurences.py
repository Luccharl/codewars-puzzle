order = [1,2,3,1,2,1,2,3]
n = 1
occurences = []


for num in order:
    if num not in occurences:
        occurences.append(num)
    elif num in occurences and occurences.count(num) < n:
        occurences.append(num)

print(occurences)