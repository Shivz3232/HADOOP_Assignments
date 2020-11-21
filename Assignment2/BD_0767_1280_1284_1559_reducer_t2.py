#!/usr/bin/python3

import sys

ranks = dict()
adj_list = dict()
destinations_set = set()

for line in sys.stdin:
	line = line.strip()

	node, rank, destinations = line.split('\t', 2)
	destinations = destinations.split(',')
	
	adj_list[node] = destinations
	ranks[node] = float(rank)
	destinations_set.update(destinations)

keys = adj_list.keys()
transition_matrix = dict()

for node in keys:
	if (node not in destinations_set):
		transition_matrix[node] = [0]
	numOfDestinations = len(adj_list[node])
	for destination in adj_list[node]:
		if destination in keys:
			temp = transition_matrix.keys()

			if destination in temp:
				transition_matrix[destination].append((ranks[node] / float(numOfDestinations)))
			else:
				transition_matrix[destination] = list()
				transition_matrix[destination].append((ranks[node] / float(numOfDestinations)))

keys = sorted(transition_matrix.keys())

for node in keys:
	print("%s, %.5f" % (node, 0.15 + 0.85 * sum(transition_matrix[node])))