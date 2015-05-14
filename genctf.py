import os, sys

if len(sys.argv) != 4:
	sys.stderr.write('Usage: python genctf.py example-ctf-2015/ info \'Example CTF\'')
	sys.exit(4)

ctfrootdir = sys.argv[1]
infofile = sys.argv[2]
ctfname = sys.argv[3]

#print ctfrootdir + "/task/" + infofile

head = '# ' + ctfname + ' 2015: '
pre = ''
pre += '**Category:** \n'
pre += '**Points:** \n'
pre += '**Solves:** \n'
pre += '**Description:**\n\n'
post = """
## Write-up

(TODO)

## Other write-ups and resources

* none yet
"""
roothead = '# ' + ctfname + ' CTF write-ups'
rootdir = open(ctfrootdir+'/README.md', 'w')
rootpre = roothead + '\n'
rootpre += """
* <TODO>
* [Scoreboard](TODO) or [local alternative](TODOLOCAL)

## Completed write-ups

* none yet

## External write-ups only

* none yet

## Missing write-ups
"""
rootdir.write(rootpre)

for root, dirs, files in os.walk(ctfrootdir):
	for file in files:
		if file.endswith(infofile):
			ok = os.path.split(root)
			readme = head + ok[len(ok)-1] + "\n\n" + pre
			for line in open(os.path.join(root, file), 'rw').readlines():
				readme += "> " + line
			readme += post
			ok = root.split('/')
			taskref = ''
			for x in range(1,len(ok)-1): taskref += ok[x] + "/"
			taskref += ok[len(ok)-1]
			rootdir.write('\n'+'* ['+taskref+']('+taskref+')')
			#print taskref
			#print root + '/' + 'README.md'
			#print readme
			with open(root + '/' + 'README.md', 'w') as f:
				f.write(readme)
				f.close()
