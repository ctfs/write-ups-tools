import argparse, os, string, sys

# Parse all parameters
parser = argparse.ArgumentParser()
parser.add_argument('ctfdir', type=str, help='Directory containing all tasks and descriptions, e.g. example-ctf-2015/')
args = parser.parse_args()

# Define components of each challenge README.md:
#	Header:			Defines CTF Name and Year
#	Preamble:		Defines Categroy, Points, #Solves, Description
#	Postscript:		Contains Local and External Writeups
#
# os.walk returns: dirpath (args.ctfdir), dirnames, filenames
# For each challenge directory, create a README.md and add files >10Mb to .gitignore
missing=external=completed=''
for root, dirs, files in os.walk(args.ctfdir):
	# Get the ctf directory name, challenge type and challenge name in an array
	rootarr = root.split('/')
	if len(rootarr)!=3: continue

	# Reference to the task inside the root CTF directory, e.g. web/task1
	taskref = ''
	for x in range(1,len(rootarr)-1): taskref += rootarr[x] + "/"
	taskref += rootarr[len(rootarr)-1]


	for f in files:
		if f!='README.md': continue
		f=root+'/'+f
		ref = '['+taskref+']('+taskref+')'
		out = open(f,'r').read()
		if '## Write-up\n\n(TODO)\n\n' not in out:
			completed+='* '+ref+'\n'
		elif '## Other write-ups and resources\n\n* none yet' not in out:
			external+='* '+ref+'\n'
		else:
			missing+='* '+ref+'\n'

readme=''
orig = open(args.ctfdir+'/README.md','r').read()
for line in open(args.ctfdir+'/README.md','r'):
	if line=='## Completed write-ups\n': break
	readme+=line

readme+='## Completed write-ups\n\n'
if completed=='': completed='* none yet\n'
readme+=completed
readme+='\n## External write-ups only\n\n'
if external=='': external='* none yet\n'
readme+=external
readme+='\n## Missing write-ups\n\n'
if missing=='': missing='* none yet'
if missing[-1:]=='\n': missing=missing[:-1]
if orig[-1:]=='\n': orig=orig[:-1]
readme+=missing

if readme!=orig:
	with open(args.ctfdir+'/README.md','w') as rm:
		rm.write(readme)
