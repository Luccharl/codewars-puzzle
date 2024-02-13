from collections import Counter


g_list = [1,1,1,2,1,1]

count = Counter(g_list)

for key in count:
    if count[key] == 1:
        print(count[key])