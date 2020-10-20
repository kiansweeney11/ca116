#!/usr/bin/env python

import sys

line = sys.stdin.readline().strip()
d = {}

while 0 < len(line):
    if line not in d:
        d[line] = 1
        line = sys.stdin.readline().strip()
    else:
        d[line] += 1
        line = sys.stdin.readline().strip()

for k in d:
    if d[k] == 1:
        print k
