"""
..title..   Challenge.py
..module description..
    Objective of this module is to
..author..
    Rammurty Subrahmaniyan (ram.sanjiv@gmail.com)
..created_date..
    February 4, 2020
..Python compatability..
    3.0 & above

For more help, import this module, and run help(<moduleName>)

"""

#!/usr/local/bin/python

import sys  # the sys module
import os
import re


def hasattr(str, list):
    expr = re.compile(str)
    # yield the elements
    return [elem for elem in list if expr.match(elem)]


is_word = dict()
FH = open(sys.argv[1])

re.compile(r'<(\w+)>', re.compile(r'^word[\s\w\S]+\n$')
for strLine in FH.readlines():
    # is_word.setdefault(''.join(sorted(strLine[12:strLine.find('>')].upper())),[]).append(strLine[:-1])   BUG
    is_word.setdefault(''.join(sorted(strLine[12:strLine.find('>')].upper())), []).append(strLine)

basestring = str()

for ARGV in sys.argv[2:]:
    print(f"\n*** {ARGV}\n")

    diffpatletters = re.compile(u'[a-zA-Z]').findall(ARGV.upper())

    diffpat = '.*' + '(.*)'.join(sorted(diffpatletters)) + '.*'

    for KEY in hasattr(diffpat,is_word.keys()):

       SUBKEY = KEY
       for X in diffpatletters:
         SUBKEY = SUBKEY.replace(X,'',1)

       if SUBKEY in is_word:
          basestring += "{:>50} -> {}\n".format(is_word[KEY], is_word[SUBKEY])

print(basestring + "\n")

# end
