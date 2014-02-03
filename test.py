#!/usr/bin/env python
import pprint
import eurdep

with open('data/IS20131215-reitr.EUR') as f:
    data = f.read()
    result = eurdep.load(data)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(result)
