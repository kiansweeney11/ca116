#!/usr/bin/env python

a = []

s = raw_input()
while s != "end":
    a.append(s)
    s = raw_input()

n = raw_input()
i = 0
while n != "end":
    i = 0
    if i < len(a) and a[int(n)] == a[int(i)]:
        i += 1
    print a[int(n)]
    n = raw_input()
