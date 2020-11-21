#!/usr/bin/python3

import sys

adj_list = dict()
ranks = dict()
destinations_set = set()

for line in sys.stdin:
	line = line.strip()
	source, destinations = line.split('\t', 1)
	adj_list[source] = destinations

path = sys.argv[1]
f = open(path, 'r')
for line in f:
	line.strip()
	node, rank = line.split(',', 1)
	rank = float(rank.strip())
	ranks[node] = rank

keys = adj_list.keys()

for node in keys:
	print(node+'\t'+str(ranks[node])+'\t'+adj_list[node])

# for node in keys:
# 	if (node not in destinations_set):
# 		print(node+'\t'+str(0.0))
# 	numOfDestinations = len(adj_list[node])
# 	for destination in adj_list[node]:
# 		if destination in keys:
# 			print(destination+'\t'+str(ranks[node] / float(numOfDestinations)))