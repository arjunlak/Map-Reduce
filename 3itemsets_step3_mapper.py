#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# a transaction has multiple items
	items = line.split(" ")

	# read the candidate 3-itemsets from distributed cache
	f = open('candidates', 'r')

	for  candidates in f:
		# remove leading and trailing whitespace
		candidates = candidates.strip()
		cand_itemset = candidates.split("\t")
		
		if set(cand_itemset).issubset(set(items)): 
			print ('%s\t%s\t%s\t%s' % (cand_itemset[0], cand_itemset[1], cand_itemset[2], 1))
	f.close() 
