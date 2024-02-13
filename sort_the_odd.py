n_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
odd_list = []

for i,num in enumerate(n_array):
    if num % 2 != 0:
        odd_list.append(num)

odd_list.sort()

for i,num in enumerate(n_array):
    if num % 2 == 0:
        odd_list.insert(i, num)
        
print(odd_list)