#!/usr/bin/env python

import sys

current_item1 = None
current_item2_list = []

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	item1, item2 = line.split('\t', 1)

	item1 = int(item1)
	item2 = int(item2)
	
	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
	if current_item1 == item1:
		current_item2_list.append(item2)
	else:
		if current_item1:
			# write result to STDOUT
			for x in current_item2_list:
				for y in current_item2_list:
					if x<y: print('%s\t%s\t%s' % (x, y, current_item1))
		current_item2_list = [item2]
		current_item1 = item1

if current_item1:
	for x in current_item2_list:
		for y in current_item2_list:
			if x<y: print('%s\t%s\t%s' % (x, y, current_item1))
