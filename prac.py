"""for the shell  . ./venv/bin/activate"""

from bs4 import BeautifulSoup
from mathematicians import simple_get
"""from the blog"""
raw_html = simple_get('https://realpython.com/blog/')

"""----len(raw_html)"""
g_html = simple_get('https://soundcloud.com/guardianscienceweekly')
a_html = simple_get('https://soundcloud.com/a16z')
r_html = simple_get('https://www.reddit.com/r/artificial/')
t_html = simple_get('https://soundcloud.com/techemergence')

ag_html = BeautifulSoup(g_html, 'html.parser')
aa_html = BeautifulSoup(a_html, 'html.parser')
"""ar_html = BeautifulSoup(r_html, 'html.parser')"""
at_html = BeautifulSoup(t_html, 'html.parser')

"""for i, li in enumerate(ag_html.select('li')):"""
"""    print (i, li.text)"""
print("a16z")
for i, a in enumerate(aa_html.select('a')): 
    if i < 20:
        print (i, a.text)
print("techemergence")
for i, a in enumerate(at_html.select('a')):
    if i < 20:
        print (i, a.text)