import re

stats = '1|15|59, 1|47|6, 01|17|20, 1|32|34, 2|17|17'
stat_list = stats.split()

stats_in_secs = []

for t in stat_list:
    time_pattern = re.compile(r'\d?\d')
    match_obj = time_pattern.findall(t)

    hr,mins,secs = match_obj
    mins = int(mins) + int(hr) * 60
    secs = int(secs) + mins * 60
    
    stats_in_secs.append(secs)

stats_in_secs.sort()
range = stats_in_secs[-1] - stats_in_secs[0]
average = sum(stats_in_secs) // len(stats_in_secs) 
middle = len(stats_in_secs) >> 1

if len(stats_in_secs) & 1:
    median = stats_in_secs[middle]
else:
    median = (stats_in_secs[middle-1] + stats_in_secs[middle]) // 2
    

print(f'range : {range} | average: {average} | median: {median}')