import sys, BeautifulSoup

# TODO: Use requests instead of copying the scoreboard table with the console... :)
soup = ''
with open('./scoreboard','r') as myfile:
	soup = myfile.read().replace('\n', '')

soup = BeautifulSoup.BeautifulSoup(soup)
scoreboard = ''
for tr in soup.findAll('tr'):
	tds = tr.findAll('td')
	if len(tds) != 5: continue
	print tds[2].a.contents[0].encode('utf8').ljust(30) + ' ' + tds[3].contents[0].encode('utf8').ljust(8)
