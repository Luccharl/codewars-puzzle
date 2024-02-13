import re

filename = '1231231223123131_myFile.tar.gz2'
filename_pattern = re.compile(r'(\d+_?)(.*)\.([A-Za-z0-9]+)')
match_obj = filename_pattern.findall(filename)

print(match_obj[0][1])