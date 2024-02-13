arr = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
count = 0
for num in arr:
    if num == 0:
        count += 1
        
for zero in range(count):
    arr.remove(0)
    arr.append(0)
print(arr)
        