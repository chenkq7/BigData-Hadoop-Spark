#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import json

for line in sys.stdin:
    line = line.strip()
    record = json.loads(line)
    print('%s\t%s' % (record[0], record[1]))
