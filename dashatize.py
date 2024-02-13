import re
n = 274

pattern_n = re.compile('[24680]*?([13579])[24680]*?')
match_obj = pattern_n.findall(str(n))

print(match_obj)