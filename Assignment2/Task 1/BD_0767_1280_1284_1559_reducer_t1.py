#!/usr/bin/python3

import sys

dict_nodes_incoming = dict()

path = sys.argv[1]

for line in sys.stdin:
	line = line.strip("\n")

	parent, child= line.split('\t', 1)

	temp = dict_nodes_incoming.keys()

	if (parent in temp):
		dict_nodes_incoming[parent].append(child)

	else:
		dict_nodes_incoming[parent] = list()
		dict_nodes_incoming[parent].append(child)

file_object = open(path, "w")

keys = sorted(dict_nodes_incoming.keys())

for i in keys:
	file_object.write("%s,1\n" % i)
	sys.stdout.write("%s\t%s\n" % (i, ','.join(sorted(dict_nodes_incoming[i]))))

file_object.close()