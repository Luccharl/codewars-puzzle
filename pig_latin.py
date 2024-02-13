text = 'Barba non facit philosophum !'
punc = '!.?'

words = text.split()

for word in range(len(words)):
    first_letter = words[word][0]
    if first_letter not in punc:
        words[word] = words[word].replace(first_letter, '', 1)
        words[word] += first_letter + 'ay'

print(' '.join(words))
    