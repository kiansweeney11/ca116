#!/usr/bin/env python

header = raw_input()

i = 0
j = 0
k = 0
while i < len(header):
    k = j + 1
    while k < len(header) and not header[k] == ",":
        k += 1

    if j < len(header):
        print header[j:k]

    j = k + 1

    i += 1
