string = '4of Fo1r pe6ople g3ood th5e the2'
words = string.split()
ordered = ''


for num in range(10):
    for word in words:
        if str(num) in word:
            print(word)