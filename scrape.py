## web scraping with BeautifulSoup

from BeautifulSoup import BeautifulSoup
import urllib
r = urllib.urlopen('http://chemgroups.northwestern.edu/chen_group/group.htm#alumni').read()
soup = BeautifulSoup(r)
print type(soup)

print soup.prettify()
