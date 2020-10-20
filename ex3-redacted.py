#!/usr/bin/env python

import sys
d = {}

with open("banned.txt") as f:
    line = f.readline().strip()
    while 0 < len(line):
        if line not in d:
            d[line] = True
            line = f.readline().strip()
        else:
            line = f.readline().strip()

lines = sys.stdin.readlines()
i = 0
sentence = ""
while i < len(lines):
    words = lines[i].strip().split()
    j = 0
    while j < len(words):
        if words[j] in d:
            words[j] = len(words[j]) * "*"
        j += 1
    sentence += " ".join(words) + "\n"
    i += 1

sys.stdout.write(sentence + "".join(lines[i:]))
