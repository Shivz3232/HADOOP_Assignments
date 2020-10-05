#!/usr/bin/python3

import sys

for line in sys.stdin:
	if (line.startswith('#')):
		continue
	line = line.strip()
	words = line.split('\t')
	print (words[0]+'\t'+words[1])
