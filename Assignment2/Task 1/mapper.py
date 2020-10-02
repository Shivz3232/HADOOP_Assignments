#!/usr/bin/env python
"""mapper"""

import sys

# Input comes form STDIN (Standard Input)
for line in sys.stdin:

    # Trim the leading and trailing spaces, and new line
    line = line.strip()

    # Extract the from node and the to node
    nodes = line.split('\t')
    start = nodes[0]
    to = nodes[1]

    # Send the from & to node to reducer through STDOUT (Standard Output)
    print(start+'\t'+to)
