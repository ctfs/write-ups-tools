# Generate a CTF directory/skeleton

Use this tool to generate a CTF skeleton.

This is how I usually maintain a new CTF directory/skeleton

* Create an empty directory for the CTF, ending with the current year, e.g. `example-ctf-2015/`
* Create an empty directory in this new CTF directory for each task category, e.g. `mkdir crypto web misc trivia`
* Create an empty for each task in the according category folder, e.g. `mkdir crypto/{rsalot, rsanne}`
* Download all CTF files during the CTF and save the description, points, original task name, solves and task category for each file in a file named `info`, e.g. `crypto/rsalot/info` and `crypto/rsanne/info`
* Generate a `README.md` for each `info` file in the CTF directory using the `genctf.py` tool, e.g. `python genctf.py example-ctf-2015/ info 'Example CTF'`
* Remove all info files (make a backup of your CTF directory just in case) using `find example-ctf-2015 -name info -delete`
* Tell git to ignore all files that are bigger than 10MBytes with `cd example-ctf-2015; find . -size +10M >> .gitignore`
* Edit each `README.md` to fill in missing information (e.g. Authors, references and solves)
* Move the CTF directory to the `write-ups-$YEAR` repo, making sure that it not yet exist
