import argparse, os, re, string, sys

# Parse all parameters
parser = argparse.ArgumentParser()
parser.add_argument('ctfdir', type=str, help='Directory containing all tasks and descriptions, e.g. example-ctf-2015/')
parser.add_argument('info', type=str, help='Default info file name containing the task description, e.g. info')
parser.add_argument('ctfname', type=str, help='Name of the CTF')
args = parser.parse_args()

# Define components of each challenge README.md:
#	Header:			Defines CTF Name and Year
#	Preamble:		Defines Categroy, Points, #Solves, Description
#	Postscript:		Contains Local and External Writeups
#
head = '# ' + args.ctfname + ' : '
#pre = '**Category:** \n'
pre = '**Points:** \n'
pre += '**Solves:** \n'
pre += '**Description:**\n\n'
post = """

## Write-up

(TODO)

## Other write-ups and resources

* none yet
"""

# Define components of each CTF root README.md:
#	RootHeader:		Defines CTF Name
#	RootPreamble:	Contains Link to CTF, scoreboards (external and local), Completed Writeups, External Writeups and Missing Writeups
roothead = '# ' + args.ctfname + ' write-ups'
rootpre = roothead + '\n'
rootpre += """
* <TODO>
* [Scoreboard](TODO) or [local alternative](TODOLOCAL)

## Repo-local write-ups

* none yet

## External write-ups only

* none yet

## Missing write-ups
"""

# Create root README.md
rootdir = open(args.ctfdir+'/README.md', 'w')
rootdir.write(rootpre)

# Create the .gitignore
gitignore = open(args.ctfdir+'/.gitignore','w')

# os.walk returns: dirpath (args.ctfdir), dirnames, filenames
# For each challenge directory, create a README.md and add files >10Mb to .gitignore
for root, dirs, files in os.walk(args.ctfdir):
	# Get the ctf directory name, challenge type and challenge name in an array
	rootarr = root.split('/')

	# Reference to the task inside the root CTF directory, e.g. web/task1
	taskref = ''
	for x in range(1,len(rootarr)-1): taskref += rootarr[x] + "/"
	taskref += rootarr[len(rootarr)-1]

	for f in files:
		# Case: info file containing the descriptions.
		if f == args.info:
			# Get all files in the directory
			farr = []
			for fr,fd,ff in os.walk(root):
				for fff in ff:
					if fff in (args.info,'README.md'): continue
					farr.append(fff)

			# Create the header of the readme with the directory name as the challenge name
			readme = head + rootarr[len(rootarr)-1] + "\n\n" + '**Category:** ' + rootarr[1].title() + '\n' + pre

			# Add the content of the info file to the readme and append the post
			for line in open(os.path.join(root, f), 'rw').readlines():
				for x in farr:
					if x in line:
						subs = '['+x+']'+'(./'+x+')'
						line = string.replace(line,x,subs)
				# http://stackoverflow.com/questions/6883049/regex-to-find-urls-in-string-in-python
				# Very inefficient, but works for now :)
				urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
				if len(urls)!=0:
					for x in urls:
						# TODO: If url is in the form <url>, don't append more brackets...
						line = string.replace(line,x,"<"+x+">")
				readme += "> " + line
				if line not in ('\n','\r\n'):
					readme+='> \n'
			if readme[-3:]=='> \n': readme=readme[:-3]
			readme += post

			# Add the task reference to the root README.md
			rootdir.write('\n'+'* ['+taskref+']('+taskref+')')

			# Create a README.md for the challenge
			with open(root + '/' + 'README.md', 'w') as f:
				f.write(readme)
				f.close()
		# Case: files required for the challenge
		else:
			# Write taskref + / + filename (e.g. web/task1/bigfile.iso) to ctf-2015/.gitignore, if its size is >10MB
			fname = taskref + '/' + f
			if os.stat(os.path.join(root,f)).st_size > 10485760:
				gitignore.write(fname+'\n')
