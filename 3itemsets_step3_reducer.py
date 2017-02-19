#!/usr/bin/env python

import sys

current_item1 = None
current_item2 = None
current_item3 = None
current_count = 0

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	tokens = line.split('\t')
	item1 = tokens[0]
	item2 = tokens[1]
	item3 = tokens[2]
	count = tokens[3]
	
	# convert count (currently a string) to int
	count = int(count)

	# this IF-switch only works because Hadoop sorts map output
	# by key before it is passed to the reducer
	if current_item1 == item1 and current_item2 == item2 and current_item3 == item3:
		current_count += count
	else:
		if current_item1 and current_count >= 1000:
			# write result to STDOUT
			print('%s\t%s\t%s' % (current_item1, current_item2, current_item3))
		current_count = count
		current_item1 = item1
		current_item2 = item2
		current_item3 = item3

# do not forget to output the last item if needed!
if current_item1 and current_count >= 1000:
	print('%s\t%s\t%s' % (current_item1, current_item2, current_item3))