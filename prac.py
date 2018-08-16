"""for the shell"""

from bs4 import BeautifulSoup
from mathematicians import simple_get
"""from the blog"""
raw_html = simple_get('https://realpython.com/blog/')
len(raw_html)
"""----"""
a_html = simple_get('https://soundcloud.com/guardianscienceweekly')
ag_html = BeautifulSoup(a_html, 'html.parser')

for i, li in enumerate(ag_html.select('li')):
           print (i, li.text)