from collections import Counter
import re

text = '''In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.'''

word_pattern = re.compile(r'[A-Za-z]+\'?[a-zA-Z]?')
match = word_pattern.findall(text.lower())

print(Counter(match).most_common(3))
