import re

string = '!\napples, pears # and bananas\ngrapes\nbananas\n $apples'
markers = ["#", "$", '!']


for obj in markers:
    comment_pattern = re.compile(f'(?=\{obj}).*')
    string = comment_pattern.sub('',string)
print(string)  
 
lines = string.split('\n')
for line in range(len(lines)):
    if line == '':
        continue
    lines[line] = lines[line].strip()
 
print(lines) 
print('\n'.join(lines))


