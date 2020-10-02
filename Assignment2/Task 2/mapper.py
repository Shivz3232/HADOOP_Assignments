#!/usr/bin/python3
"""mapper"""

import sys

# Function extract the initial ranks from the v file
def initRanks(path):
    # Define a dictionary to hold the node-rank relation
    ranks = dict()

    file = open(path)

    line = file.readline()
    while line:
        temp = line.split(',')

        #Rank of the node 
        rank = int(temp[1])

        # Add the node as the key and the rank as the value to the dictionary
        ranks[temp[0]] = rank

        line = file.readline()

    file.close()

    return ranks

# Initiate the ranks
ranks = initRanks("./v.txt")

# Use the initial ranks and the adjacency matrix to calculate the X. ( X: Vi(t-1) / Number of nodes pointing to the current node )
#Where Vi(t) -> Rank of the node i at iteration t.
for line in sys.stdin:

    # Node, and list of nodes reachable from current node
    source, destinations = line.strip().split('\t', 1)
    destinations = destinations.split(',')

    numberOfDestinations = len(destinations)    # Nuber of nodes current node is pointing to

    for destination in destinations:
        print(destination+"\t",(ranks[source] / numberOfDestinations))
