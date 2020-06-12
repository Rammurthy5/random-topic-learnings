"""
Flashtext uses trie algorithm, and appears to be faster than regex at search, and replacing.

"""

import flashtext as ft

ft = ft.KeywordProcessor()

sample = "This is Big Apple and Big Mac alias McDonalds. / - There is a big house where 4 people lived, Ram is a Python engg" \
         "His wife shanu is a Java developer, they had two children Druv and Dahlia."
# 'add_keyword', 'add_keyword_from_file', 'add_keywords_from_dict', 'add_keywords_from_list', 'add_non_word_boundary',
# 'case_sensitive', 'extract_keywords', 'get_all_keywords', 'get_keyword', 'keyword_trie_dict',
# 'non_word_boundaries', 'remove_keyword', 'remove_keywords_from_dict', 'remove_keywords_from_list', 'replace_keywords',
#  'set_non_word_boundaries'

# Extract keywords
ft.add_keyword("Big Apple")
print(ft.extract_keywords(sample))
print(ft.extract_keywords(sample, span_info=True))

# find & replace
ft.add_keyword("Big Apple", "ManickBasha")
print(ft.replace_keywords(sample))

# add multiple keywords
ft.add_keywords_from_dict({"programming":["Python", "Java"], "members": ["Ram", "Shanu", "Druv", "Dahlia"]})
ft.add_keywords_from_list(["children"])
print(ft.extract_keywords(sample))

# Non-word character
ft.add_non_word_boundary("i")
ft.set_non_word_boundaries("i")
print(ft.extract_keywords(sample))

print(ft.keyword_trie_dict)
print(sample)
