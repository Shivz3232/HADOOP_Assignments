#!/usr/bin/env python
"""reducer"""

import sys

# Initiate a dictionary to contain a node as the key and a list of all the nodes rechable from that node
dict_nodes_incoming = dict()

# nodes list
nodes = None

# Parent node
parent = None

# Child node
child = None

# Input comes from the STDIN (Standard Input)
for line in sys.stdin:
    # Trim the leading and trailing spaces, new line
    line = line.strip()

    # Extract the parent and the child
    nodes = line.split('\t')
    parent = nodes[0]
    child = nodes[1]

    # If parent is already a key in the dictionary append the child to its list
    if (parent in dict_nodes_incoming.keys()):
        dict_nodes_incoming[parent].append(child)

    # Initiate a list with parent as the key and add the child to this list
    else:
        dict_nodes_incoming[parent] = list()
        dict_nodes_incoming[parent].append(child)

# Initiate the file descriptor for the 'v' file
file_object = open("v.txt", "w")

# Print all the nodes which are present as keys with a page rank of 1 to the file
for i in sorted(dict_nodes_incoming.keys()):
    file_object.write("%d, 1\n" % (int(i)))

# Close the file descriptor
file_object.close()

# Initiate the file descriptor for the 'adj_list' file
file_object = open("adj_list.txt", "w")

# Print the dictionary to file delimited by '\n'
for i in sorted(dict_nodes_incoming.keys()):
    file_object.write("%d    %s\n" % (int(i), dict_nodes_incoming[i]))

# Close the file descriptor
file_object.close()
