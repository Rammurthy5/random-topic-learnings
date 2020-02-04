'''
..title..   Challenge.py
..module description..
    Objective of this module is to parse the given text file on argv[1], and print the values for argv[2] and so on.
..author..
    Rammurty Subrahmaniyan (ram.sanjiv@gmail.com)
..created_date..
    February 4, 2020
..Python compatability..
    3.0 & above
For more help, import this module, and run help()
'''

#!/usr/local/bin/python3

import os
import sys
import re
import traceback
from collections import defaultdict

class TextParser:
    try:
        def __init__(self):
            if not len(sys.argv)&gt;2:
                self.usage()
            self.file = sys.argv[1]
            self.check_words = sys.argv[2:]
            self.is_word = defaultdict(list)
            self.base_string = str()
            self.file_content = list()
            self.parse_file()

        def parse_file(self):
            '''
            Method validates file path, and extracts contents into a list
            :return: None, forms a dictionary
            '''
            assert os.path.exists(self.file), 'No such File exists'
            with open(self.file) as fp:
                self.file_content = fp.readlines()
            assert self.file_content, 'No content in the File'
            for _ in self.file_content:
                regexed = re.search(r'', _)
                self.is_word[''.join(sorted(regexed.groups()[0])).upper()].append(regexed.string)
    
        def solve_regex(self):
            '''
            Method goes through check_words list, and finds it in the parsed file content.
            :return: None, forms a base string.
            '''
            check_word_sorted = map(lambda x: ''.join(sorted(x)).upper(), self.check_words)
            for _ in check_word_sorted:
                print(_)
                if _ in self.is_word:
                    self.base_string += '{:&gt;50} -&gt; {}\n'.format(_, self.is_word[_])
                    print(self.base_string)

        def usage(self):
            print('Please pass Filename with path you want to parse as arg1, and the keywords you want to search as'
                  ' rest of the arguments')
            print('For eg. ./challenge.py   ...')
            sys.exit(0)

    except AssertionError as ae:
        print(traceback.format_exc(6))
        raise ae

text_parser_obj = TextParser()
text_parser_obj.solve_regex()
