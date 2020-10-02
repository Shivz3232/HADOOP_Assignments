#!/usr/bin/python3
"""reducer"""

import sys

# node: [X]
nodes = dict()

for line in sys.stdin:
    line = line.strip()

    node, contribution = line.split('\t', 1)

    if (node in nodes.keys()):
        nodes[node].append(float(contribution))
    else:
        nodes[node] = list()
        nodes[node].append(float(contribution))

for node in sorted(nodes.keys()):
    print(node+'\t', (0.15 + 0.85 * sum(nodes[node])))
    
