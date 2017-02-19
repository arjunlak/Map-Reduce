#!/usr/bin/env python

import sys

current_item1 = None
current_item2 = None
is_frequent = False
prefix_items = []
	
# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the frequent 2-itemsets and the result of joining frequent 2-itemsets.
	items = line.split('\t')
	
	item1 = int(items[0])
	item2 = int(items[1])
		
	# this IF-switch only works because Hadoop sorts map output
	# by key (here a composite key <item1, item2>) before it is passed to the reducer
	if current_item1 != item1 or current_item2 != item2:
		if current_item1 and is_frequent:
			if len(prefix_items)>0: 
				for prefix in prefix_items: print('%s\t%s\t%s' % (prefix, current_item1, current_item2))
			
		current_item1 = item1
		current_item2 = item2
		is_frequent = False
		prefix_items = []	

	if len(items) == 2: 
		# <item1, item2> is a frequent 2-itemset
		is_frequent = True
	else:
		# the input <item1, item2, prefix> is the result of 
		# joining frequent 2-itemsets <prefix, item1> and <prefix, item2>
		prefix_items.append(int(items[2]))
	
# do not forget to output for the last composite key, if needed!
if current_item1 and is_frequent:
	if len(prefix_items)>0: 
		for prefix in prefix_items: print('%s\t%s\t%s' % (prefix, current_item1, current_item2))
			