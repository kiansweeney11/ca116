#!/usr/bin/env python

import sys

d = {}

with open("translation.txt") as f:
    line = f.readline().strip().split()
    while 0 < len(line):
        d[line[0]] = line[1]
        line = f.readline().strip().split()

word = sys.stdin.readline().strip()
while 0 < len(word):
    print d[word]
    word = sys.stdin.readline().strip()
