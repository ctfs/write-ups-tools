import argparse, requests, sys, BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('ctftimeurl', type=str, help='Ctftime Url of the CTF')
args = parser.parse_args()
r = requests.get(args.ctftimeurl)
soup = BeautifulSoup.BeautifulSoup(r.text.replace('\n',''))
scoreboard = ''
for tr in soup.findAll('tr'):
	tds = tr.findAll('td')
	if len(tds) != 5: continue
	print tds[2].a.contents[0].encode('utf8').ljust(30) + ' ' + tds[3].contents[0].encode('utf8').ljust(8)
