import re

def url_extractor(url):
    url_pattern = re.compile(r'(https?://)?(www\.)?(\w+(-\w+)?)(\.\w+)?')
    match_obj = url_pattern.search(url)
    
    return match_obj.groups()

if __name__ == '__main__':
    print(url_extractor('https://youtube-zite.com'))