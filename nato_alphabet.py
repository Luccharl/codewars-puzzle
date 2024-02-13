string = 'If, you can read this?'

nato = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 
        'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike', 
        'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 
        'Uniform', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']

punctuation = ',.?!'

decoded = ''

for char in string.upper():
    if char in punctuation:
        decoded += ' ' + char
    for code in nato:
        if code.startswith(char):
            decoded += ' ' + code
print(decoded.strip())