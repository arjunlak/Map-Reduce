#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	
	# parse the frequent 2-itemsets
	tokens = line.split('\t')
	item1 = tokens[0]
	item2 = tokens[1]
	
	item1 = int(item1)	
	item2 = int(item2)
	
	# The input file must be frequent 2-itemsets.
	# Each line should have a pair of items "item1 item2",
	# in which item1 < item2.
	print('%s\t%s' % (item1, item2))
