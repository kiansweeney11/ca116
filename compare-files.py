#!/usr/bin/env python

import sys

with open(sys.argv[1]) as file1:
    with open(sys.argv[2]) as file2:
        line1 = file1.readline().strip()
        line2 = file2.readline().strip()
        count = 0
        while 0 < len(line1) and 0 < len(line2):
            if line1 == line2:
                line1 = file1.readline().strip()
                line2 = file2.readline().strip()
                count += 1

        i = 0
        while i < len(line1) and i < len(line2) and line1[i] != line2[i]:
            i += 1
        print count, i

