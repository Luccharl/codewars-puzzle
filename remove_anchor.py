# import re

# def remove_url_anchor(url):
#     url_re = re.compile(r'((.*)?(\w+)\.(\w\w\w?)((.*)?(?=#)|(.*)(?=#)?)?)')
#     match_obj = url_re.findall(url)
    
#     return match_obj[0][0]   

import re

def remove_url_anchor(url):
    return url.split('#')[0]

remove_url_anchor('bacon.gov#fenduan')