#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# a transaction has multiple items
	items = line.split(" ")
	
	for item1 in items:
		item1 = int(item1)
		for item2 in items:
			item2 = int(item2)
			if item1 < item2:	print('%s\t%s\t%s' % (item1, item2, 1))
